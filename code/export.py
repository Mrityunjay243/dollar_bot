import helper
import logging
from matplotlib import pyplot as plt
import csv
import pandas as pd

def export_to_csv(user_history, file_path):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Date", "Category", "Amount"])
        for record in user_history:
            date_str, category, amount_str = record.split(",")
            amount = float(amount_str)
            csv_writer.writerow([date_str, category, amount])

def export_to_excel(user_history, file_path):
    data = []
    for record in user_history:
        date_str, category, amount_str = record.split(",")
        amount = float(amount_str)
        data.append({"Date": date_str, "Category": category, "Amount": amount})

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def run(message, bot):
    try:
        chat_id = message.chat.id

        input_command = message.text.split()
        export_format = input_command[1].lower() if len(input_command) > 1 else None
        export_format = 'xlsx' if export_format == 'excel' else 'csv'

        if export_format not in ['csv', 'xlsx']:
            bot.reply_to(message, "Invalid export format. Please use /export csv or /export excel.")
            return

        # Export to CSV or Excel based on user input
        file_path = f"expense_history.{export_format}"
        if export_format == 'csv':
            export_to_csv(helper.getUserHistory(chat_id), file_path)
        elif export_format == 'xlsx':
            export_to_excel(helper.getUserHistory(chat_id), file_path)

        # Send the exported file to the user
        bot.send_document(chat_id, open(file_path, "rb"))

        message = f"Done! You can download the expense history in {export_format.upper()} format."
        bot.send_message(chat_id, message)

    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops! " + str(e))
