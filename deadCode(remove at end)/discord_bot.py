# bot2.py
import os
import random
import discord
from discord import app_commands


TOKEN = 'MTE3NTk3MjE2MjI2ODU2NTU1NA.GmIqKh.BXPRBEaHZ-23GsHag-At7VM7dxlwv6KtnsK7Ac'
GUILD = 'Dollar Bot Server'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
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
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!A'):
      await message.channel.send('Hi Sussy!')

      client.run(TOKEN)


@client.event
async def on_message(message):
    
    faq_message = (
        '"What does this bot do?"\n'
        ">> DollarBot lets you manage your expenses so you can always stay on top of them! \n\n"
        '"How can I add an expense?" \n'
        ">> Type /add, then select a category to type the expense. \n\n"
        '"Can I see the history of my expenses?" \n'
        ">> Yes! Use /display to get a graphical display or /history to view a detailed summary.\n\n"
        '"I added an incorrect expense. How can I edit it?"\n'
        ">> Use /edit command. \n\n"
        '"Can I check if my expenses have exceeded the budget?"\n'
        ">> Yes! Use /budget and then select the view category. \n\n"
    )
    if message.content.startswith('/faq'):
        await message.channel.send(faq_message)

@client.event
async def on_message(message):
    if message.content.startswith('/addexpense'):
        await message.channel.send("Please Add in next command with 'add <type> <amount>' ")
async def on_message(message):
    if message.content.startswith('/add'):
        print(message.content)
        await message.channel.send("Please Add in next command with 'add <type> <amount>' ") 
    
client.run(TOKEN)