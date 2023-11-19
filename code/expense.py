import telebot
import helper
import edit
from datetime import datetime

def process_expense_command(message, bot):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = ["Add", "Delete", "Update"]
    for opt in options:
        markup.add(opt)
    msg = bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    bot.register_next_step_handler(msg, expense_option_selection, bot)

def expense_option_selection(message, bot):
    selected_option = message.text
    if selected_option == "Add":
        select_expense_category(message, bot)
    elif selected_option == "Delete":
        delete_expense(message, bot)  # Call the delete_expense function.
    elif selected_option == "Update":
        edit.run(message, bot)  # This calls the edit functionality
    else:
        bot.send_message(message.chat.id, "Invalid option. Please try again.")

def select_expense_category(message, bot):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    categories = helper.getSpendCategories()  # Retrieve the list of categories.
    for c in categories:
        markup.add(c)
    msg = bot.send_message(message.chat.id, "Select Category for expense:", reply_markup=markup)
    bot.register_next_step_handler(msg, expense_category_selected, bot)

def expense_category_selected(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category not in helper.getSpendCategories():
            bot.send_message(chat_id, "Invalid", reply_markup=telebot.types.ReplyKeyboardRemove())
            raise Exception(f'Sorry, I don\'t recognize this category "{selected_category}"!')

        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(chat_id, f"How much did you spend on {selected_category}?", reply_markup=markup)
        bot.register_next_step_handler(msg, record_expense, selected_category, bot)
    except Exception as e:
        bot.reply_to(message, "Oh no! " + str(e))

def record_expense(message, category, bot):
    try:
        chat_id = message.chat.id
        
        input_params = message.text.split()
        amount_entered = input_params[0]
        from_currency = input_params[1].upper() if len(input_params) > 1 else 'USD'

        amount_entered = helper.convertCurrency(amount_entered, from_currency)
        
        amount_value = helper.validate_entered_amount(amount_entered)  # validate

        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")

        date_of_entry = datetime.today().strftime(helper.getDateFormat() + " " + helper.getTimeFormat())
        record_to_be_added = "{},{},{}".format(str(date_of_entry), category, str(amount_value))
        
        helper.write_json(add_user_record(chat_id, record_to_be_added))

        bot.send_message(chat_id, f"You have spent ${amount_value} for {category} on {date_of_entry}")
        helper.display_remaining_budget(message, bot, category)
    except Exception as e:
        bot.reply_to(message, "Oh no. " + str(e))

def delete_expense(message, bot):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    expenses = helper.getUserHistory(message.chat.id)  # Get user's expense history.
    for expense in expenses:
        markup.add(expense)
    
    msg = bot.send_message(message.chat.id, "Select the expense to delete:", reply_markup=markup)
    bot.register_next_step_handler(msg, confirm_delete_expense, bot)

def confirm_delete_expense(message, bot):
    selected_expense = message.text
    user_list = helper.read_json()
    chat_id = message.chat.id
    user_data = user_list.get(str(chat_id))
    if user_data:
        expenses = user_data.get("data", [])
        updated_expenses = [expense for expense in expenses if selected_expense not in expense]
        user_data["data"] = updated_expenses
        helper.write_json(user_list)
        bot.send_message(chat_id, f"Expense '{selected_expense}' has been deleted.")
    else:
        bot.send_message(chat_id, "No expense found for deletion.")
    
    helper.display_remaining_budget(message, bot, "")  # You can specify the category here.

def add_user_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()
    user_list[str(chat_id)]["data"].append(record_to_be_added)
    return user_list
