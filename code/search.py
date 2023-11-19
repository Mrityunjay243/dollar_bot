import helper
import logging
from telebot import types

# === Documentation of search.py ===

def run(message, bot):
    categories_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for category in helper.spend_categories:
        categories_keyboard.add(category)
    
    message = bot.send_message(message.chat.id, "Select a spend category:", reply_markup=categories_keyboard)
    bot.register_next_step_handler(message, post_select_category, bot)

def post_select_category(message, bot):
    try:
        helper.read_json()
        selected_category = message.text
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        spend_total_str = ""
        if user_history is None:
            raise Exception("Sorry! No spending records found!")
        spend_total_str = "Here is your spending history by category : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_history:
                if rec.split(',')[1] == selected_category:
                    spend_total_str += str(rec) + "\n"
        bot.send_message(chat_id, spend_total_str)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))