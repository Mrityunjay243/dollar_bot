#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import telebot
import time
import helper
import edit
import history
import pdf
import display
import estimate
import delete
import category_delete
import category_add
import category_view
import add
import budget
import search
import export
import support
import csv_export
from datetime import datetime
from jproperties import Properties
from expense import process_expense_command

configs = Properties()

with open("user.properties", "rb") as read_prop:
    configs.load(read_prop)

option = {}

api_token = str(configs.get("api_token").data)
bot = telebot.TeleBot(api_token)

telebot.logger.setLevel(logging.INFO)

option = {}

# === Documentation of code.py ===

# Define listener for requests by user


def listener(user_requests):
    """
    listener(user_requests): Takes 1 argument user_requests and logs all user
    interaction with the bot including all bot commands run and any other issue logs.
    """
    for req in user_requests:
        if req.content_type == "text":
            print(
                "{} name:{} chat_id:{} \nmessage: {}\n".format(
                    str(datetime.now()),
                    str(req.chat.first_name),
                    str(req.chat.id),
                    str(req.text),
                )
            )

    message = (
        ("Sorry, I can't understand messages yet :/\n"
         "I can only understand commands that start with /. \n\n"
         "Type /faq or /help if you are stuck.")
    )

    try:
        helper.read_json()
        global user_list
        chat_id = user_requests[0].chat.id

        if user_requests[0].text[0] != "/":
            bot.send_message(chat_id, message)
    except Exception:
        pass


bot.set_update_listener(listener)


@bot.message_handler(commands=["help"])
def help(m):

    helper.read_json()
    global user_list
    chat_id = m.chat.id

    message = "Here are the commands you can use: \n"
    commands = helper.getCommands()
    for c in commands:
        message += "/" + c + ", "
        # message += commands[c] + "\n\n"
    message += "\nUse /menu for detailed instructions about these commands."
    bot.send_message(chat_id, message)


@bot.message_handler(commands=["faq"])
def faq(m):

    helper.read_json()
    global user_list
    chat_id = m.chat.id

    faq_message = (
        ('"What does this bot do?"\n'
         ">> DollarBot lets you manage your expenses so you can always stay on top of them! \n\n"
         '"How can I add an epxense?" \n'
         ">> Type /add, then select a category to type the expense. \n\n"
         '"Can I see history of my expenses?" \n'
         ">> Yes! Use /display to get a graphical display, or /history to view detailed summary.\n\n"
         '"I added an incorrect expense. How can I edit it?"\n'
         ">> Use /edit command. \n\n"
         '"Can I check if my expenses have exceeded budget?"\n'
         ">> Yes! Use /budget and then select the view category. \n\n")
    )
    bot.send_message(chat_id, faq_message)


# defines how the /start and /help commands have to be handled/processed
@bot.message_handler(commands=["start", "menu"])
def start_and_menu_command(m):
    """
    start_and_menu_command(m): Prints out the the main menu displaying the features that the
    bot offers and the corresponding commands to be run from the Telegram UI to use these features.
    Commands used to run this: commands=['start', 'menu']
    """
    helper.read_json()
    global user_list
    chat_id = m.chat.id

    # print('receieved start or menu command.')
    # text_into = "Welcome to the Dollar Bot!"

    text_intro = (
        ("Welcome to the Dollar Bot! \n"
         "DollarBot can track all your expenses with simple and easy to use commands :) \n"
         "Here is the complete menu. \n\n")
    )
    # "Type /faq or /help to get stated."

    commands = helper.getCommands()
    for (
        c
    ) in (
        commands
    ):  # generate help text out of the commands dictionary defined at the top
        text_intro += "/" + c + ": "
        text_intro += commands[c] + "\n\n"
    bot.send_message(chat_id, text_intro)
    return True


# defines how the /new command has to be handled/processed
@bot.message_handler(commands=["category"])
def command_add(message):
    """
    command_add(message) Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls add.py to run to execute
    the add functionality. Commands used to run this: commands=['add']
    """
    add.run(message, bot)


# function to fetch expenditure history of the user


@bot.message_handler(commands=["pdf"])
def command_pdf(message):
    """
    command_history(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls pdf.py to run to execute
    the add functionality. Commands used to run this: commands=['pdf']
    """
    pdf.run(message, bot)


# function to fetch expenditure history of the user
@bot.message_handler(commands=["history"])
def command_history(message):
    """
    command_history(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls history.py to run to execute
    the add functionality. Commands used to run this: commands=['history']
    """
    history.run(message, bot)


# function to edit date, category or cost of a transaction
@bot.message_handler(commands=["edit"])
def command_edit(message):
    """
    command_edit(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls edit.py to run to execute
    the add functionality. Commands used to run this: commands=['edit']
    """
    edit.run(message, bot)


# function to display total expenditure
@bot.message_handler(commands=["display"])
def command_display(message):
    """
    command_display(message): Takes 1 argument message which contains the message from the user
    along with the chat ID of the user chat. It then calls display.py to run to execute the add functionality.
    Commands used to run this: commands=['display']
    """
    display.run(message, bot)


# function to estimate future expenditure
@bot.message_handler(commands=["estimate"])
def command_estimate(message):
    estimate.run(message, bot)


# handles "/delete" command
@bot.message_handler(commands=["delete"])
def command_delete(message):
    """
    command_delete(message): Takes 1 argument message which contains the message from the user
    along with the chat ID of the user chat. It then calls delete.py to run to execute the add functionality.
    Commands used to run this: commands=['display']
    """
    delete.run(message, bot)

# exporting to csv
@bot.message_handler(commands=["export"])
def handle_export(message):
    user_id = str(message.from_user.id)
    user_expenses = []  # Replace this with actual user expense data

    if user_expenses:
        exported_file = export_to_csv(user_id, user_expenses)
        bot.send_document(message.chat.id, open(exported_file, "rb"))
    else:
        bot.send_message(message.chat.id, "No expenses to export.")



@bot.message_handler(commands=['expense'])
def handle_expense_command(message):
    process_expense_command(message, bot)



@bot.message_handler(commands=["budget"])
def command_budget(message):
    budget.run(message, bot)

@bot.message_handler(commands=['search'])
def handle_search(message):
    search.run(message, bot)

@bot.message_handler(commands=['export'])
def handle_search(message):
    export.run(message, bot)


@bot.message_handler(commands=["support"])
def command_support(message):
    support.run(message, bot)


def addUserHistory(chat_id, user_record):
    global user_list
    if not (str(chat_id) in user_list):
        user_list[str(chat_id)] = []
    user_list[str(chat_id)].append(user_record)
    return user_list


def main():
    """
    main() The entire bot's execution begins here. It ensure the bot variable begins
    polling and actively listening for requests from telegram.
    """
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.exception(str(e))
        time.sleep(3)
        print("Connection Timeout")


if __name__ == "__main__":
    main()