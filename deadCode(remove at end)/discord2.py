import asyncio
import discord
from discord.ext import commands
from discordUser import User
from discord.ui import Select, View
import os
import pathlib
import pickle
import re
from datetime import datetime
from tabulate import tabulate

BOT_TOKEN = 'MTE3NTk3MjE2MjI2ODU2NTU1NA.GmIqKh.BXPRBEaHZ-23GsHag-At7VM7dxlwv6KtnsK7Ac'
CHANNEL_ID = '1175972668118405133'

bot = commands.Bot(command_prefix="#", intents=discord.Intents.all())
user_list = {}

@bot.event
async def on_ready():
    """
    An event handler for the "on_ready" event.
    This function is called when the bot has successfully connected to the Discord server and is ready to operate. It sends a welcome message to a specific channel and then calls the "menu" 
    function to display a menu, likely for user interaction.

    Parameters: 
    - None

    Returns: 
    - None
    """
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send("Hello ! Welcome to FinBot - a simple solution to track your expenses! \n\n")
    await menu(channel)

@bot.command()
async def menu(ctx):
    """
    Handles the 'menu' command to display a list of available commands and their descriptions in an embed window.

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.

    Returns:
    - None
    """
    em = discord.Embed(title="FinBot", description="Here is a list of available commands, please enter a command of your choice with a prefix '#' so that I can assist you further.\n ",color = discord.Color.teal())
    em.add_field(name="**#menu**", value="Displays all commands and their descriptions", inline=False)
    em.add_field(name="**#add**", value="Record/Add a new spending", inline=False)
    em.add_field(name="**#display**", value="Show sum of expenditure for the current day/month", inline=False)
    em.add_field(name="**#history**", value="Display spending history", inline=False)
    em.add_field(name="**#delete**", value="Clear/Erase all your records", inline=False)
    em.add_field(name="**#edit**", value="Edit/Change spending details", inline=False)
    em.add_field(name="**#budget**", value="Set budget for the month", inline=False)
    em.add_field(name="**#chart**", value="See your expenditure in different charts", inline=False)
    
    await ctx.send(embed=em)


@bot.command()
async def add(ctx):
    """
    Handles the commands 'add'. To add a transaction to the user records. 

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.

    Returns: None
    """
     
    if CHANNEL_ID not in user_list.keys(): user_list[CHANNEL_ID] = User(CHANNEL_ID)
    try: await select_date(ctx)

    except Exception as ex:
        print("exception occurred:"+str(ex))
        await ctx.send("Request cannot be processed. Please try again with correct format!")


async def select_date(ctx):
    '''
    Function to get date selection from user. This function is invoked from the add to
    enter the date of expense to be added.

    :param ctx - Discord context window
    :param Bot - Discord Bot object
    :param date - date message object received from the user
    :type: object
    :return: None

    '''
    dateFormat = "%m-%d-%Y"
    curr_day = datetime.now()
    await ctx.send("Enter day")
    await ctx.send(f"\n\tExample day in format mm-dd-YYYY: {curr_day.strftime(dateFormat)}\n")
    def check(msg): return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        date_message = await bot.wait_for('message', check=check, timeout=60)
        date_str = date_message.content.strip()
        month, date, year = map(int, date_str.split('-'))

        # Call the next function with the date, month, and year
        await process_date(ctx, date, month, year)
    except asyncio.TimeoutError: await ctx.send("You took too long to respond. Please try again.")

async def process_date(ctx, date, month, year):
    '''
    Process the date, month, and year here
    You can perform any necessary calculations or operations
    For example, you can convert them to a datetime object
    :param ctx - Discord context window
    :param date - date string
    :param month - month string
    :param year - year string
    :type: object
    :return: None
    '''
    
    try:
        date_obj = datetime(int(year), int(month), int(date))
        await ctx.send(f"Selected Date: {date_obj.strftime('%m-%d-%Y')}")
        await select_category(ctx, date_obj)
    except ValueError: await ctx.send("Invalid date, month, or year. Please enter valid values.")

async def select_category(ctx, date):
    """
    Function to enable category selection via a custom-defined category dropdown. This function is invoked from the 'select_date' function 
    to select the category of expense to be added. It utilizes the Select and View classes from discord.ui and a callback to handle the 
    interaction response.

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.
    - date (discord.Message): The date message object received from the user.

    Returns:
    - None
    """

    spend_categories = user_list[CHANNEL_ID].spend_categories
    select_options = [discord.SelectOption(label=category) for category in spend_categories]
    select = Select(placeholder="Select a category", max_values=1,min_values=1, options=select_options)
    
    async def my_callback(interaction):
        await interaction.response.send_message(f'You chose: {select.values[0]}')
        await asyncio.sleep(0.5)
        if select.values[0] not in spend_categories:
            await ctx.send("Invalid category")   
            raise Exception('Sorry I don\'t recognise this category "{}"!'.format(select.values[0]))

        await post_category_selection(ctx, date, select.values[0])

    select.callback = my_callback
    
    view = View(timeout=90)
    view.add_item(select)
  
    await ctx.send('Please select a category', view=view)

async def post_category_selection(ctx, date_to_add,category):
    """
    Receives the category selected by the user and then asks for the amount spent. If an invalid category is given,
    an error message is displayed, followed by a command list. If the category given is valid, 'post_amount_input' is
    called next to collect the amount spent.

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.
    - date_to_add (object): The date of the purchase.
    - category (str): The selected category for the expense.

    Returns:
    - None
    """
    try:
        selected_category = category
        
        await ctx.send(f'\nHow much did you spend on {selected_category}')
        amount = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

        await post_amount_input(ctx, amount.content,selected_category,date_to_add)
    except Exception as ex:
        print(str(ex), exc_info=True)
        await ctx.send("Request cannot be processed. Please try again with correct format!")

async def post_amount_input(ctx, amount_entered,selected_category,date_to_add):
    """
    Receives the amount entered by the user and adds it to the transaction history. An error is displayed if the entered
    amount is zero. Else, a message is shown that the transaction has been added.

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.
    - amount_entered (str): The amount entered by the user for the transaction.
    - selected_category (str): The category of the expense selected by the user.
    - date_to_add (str): The date of the transaction in a string format.

    Returns:
    - None
    """
   
    try:
        amount_value = user_list[CHANNEL_ID].validate_entered_amount(amount_entered)  # validate
        if amount_value == 0:  raise Exception("Spent amount has to be a non-zero number.") # cannot be $0 spending

        category_str, amount_str = (selected_category,format(amount_value, ".2f"))
        user_list[CHANNEL_ID].add_transaction(date_to_add, selected_category, amount_value, CHANNEL_ID)
        total_value = user_list[CHANNEL_ID].monthly_total()
        add_message = f"The following expenditure has been recorded: You have spent ${amount_str} for {category_str} on {date_to_add}"

        if user_list[CHANNEL_ID].monthly_budget > 0:
            if total_value > user_list[CHANNEL_ID].monthly_budget: await ctx.send("*You have gone over the monthly budget*")
            elif total_value == user_list[CHANNEL_ID].monthly_budget: await ctx.send("*You have exhausted your monthly budget. You can check/download history*")
            elif total_value >= 0.8 * user_list[CHANNEL_ID].monthly_budget: await ctx.send("*You have used 80% of the monthly budget*")

        await ctx.send(add_message)
    except Exception as ex:
        print(str(ex), exc_info=True)
        await ctx.send("Request cannot be processed. Please try again with correct format!")

@bot.command()
async def display(ctx):
    """
    Handles the command 'display'. If the user has no transaction history, a message is displayed. If there is
    transaction history, user is given choices of time periods to choose from. The function 'display_total' is called
    next.

    Parameters:
    - ctx (discord.ext.commands.Context): The Discord context window.

    Returns:
    - None
    """
    if CHANNEL_ID not in user_list or user_list[CHANNEL_ID].get_number_of_transactions() == 0: await ctx.send("Oops! Looks like you do not have any spending records!")
    else:
        try:
            select_options = [discord.SelectOption(label="Day"),discord.SelectOption(label="Month"),]
            select = Select(placeholder="Select a category", max_values=1,min_values=1, options=select_options)
                
            async def my_callback(interaction):
                await interaction.response.send_message(f'You chose: {select.values[0]}')
                await asyncio.sleep(0.5)
                await display_total(ctx, select.values[0])
            
            select.callback = my_callback
            view = View(timeout=90)
            view.add_item(select)
            
            await ctx.send('Please select a category to see the total expense', view=view)

        except Exception as ex:
            print(str(ex), exc_info=True)
            await ctx.send("Request cannot be processed. Please try again with correct format!")






if __name__ == "__main__":
    try:
        # user_list = get_users()
        bot.run(BOT_TOKEN)
    except Exception as e: print(f"{e}")