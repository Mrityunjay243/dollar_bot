from datetime import datetime
import helper
import logging
from matplotlib import pyplot as plt

def calculate_total_expenses(user_history):
    total_expenses = {}
    for record in user_history:
        date, category, amount = record.split(",")
        amount = float(amount)
        if category not in total_expenses:
            total_expenses[category] = amount
        else:
            total_expenses[category] += amount
    return total_expenses

def is_overall_budget_exceeded(user_history, overall_budget):
    total_expenses = calculate_total_expenses(user_history)
    total_spent = sum(total_expenses.values())
    
    if overall_budget is not None:
        if total_spent > overall_budget:
            return True
    return False

def calculate_expenses_by_category(user_history, from_date, to_date):
    expenses_by_category = {}
    for record in user_history:
        date, category, amount = record.split(",")
        date = datetime.strptime(date.split()[0], "%d-%b-%Y")
        amount = float(amount)
        if from_date <= date and date <= to_date:
            print(from_date, date, to_date)
            if category not in expenses_by_category:
                expenses_by_category[category] = amount
            else:
                expenses_by_category[category] += amount
    return expenses_by_category

def display_pie_chart(user_history, user_budget, from_date, to_date):
    expenses_by_category = calculate_expenses_by_category(user_history, from_date, to_date)
    categories = expenses_by_category.keys()
    expenses = expenses_by_category.values()
    dates = []
    
    # Extract the dates for each category
    for category in categories:
        dates_str = [
            record.split(',')[0] 
            for record in user_history 
            if category in record 
            and from_date <= datetime.strptime(record.split(',')[0].split()[0].split()[0], "%d-%b-%Y") 
            and datetime.strptime(record.split(',')[0].split()[0].split()[0], "%d-%b-%Y") <= to_date
        ]
        dates.append(dates_str)

    fig, ax1 = plt.subplots(2, 1, figsize=(8, 8))

    # Create the pie chart
    ax1[0].pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
    ax1[0].set_title("Expenses by Category")
    ax1[0].axis('equal')

    # Add text below the pie chart with categories, expenses, and dates
    text = "Categorywise Expenses:\n"
    for category, expense, date_list in zip(categories, expenses, dates):
        date_str = ", ".join(date_list)
        text += f"{category}: ${expense:.2f} (on {date_str})\n"

    # Create a subplot for budget-related information
    ax2 = ax1[1]

    # Check if the overall budget is exceeded
    if user_budget is not None:
        user_budget = float(user_budget)
        total_expenses = sum(expenses)
        budget_str = f"Overall Budget: ${user_budget:.2f}"
        text += f"\n{budget_str}"
        if total_expenses > user_budget:
            budget_status = "You are over budget."
        else:
            budget_status = "You are within budget."
        text += f"\n{budget_status}"
    
    ax2.axis('off')
    ax2.text(0.5, 0.5, text, horizontalalignment='center', verticalalignment='center', fontsize=14)

    return fig

def run(message, bot):
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        user_budget = helper.getOverallBudget(chat_id)
        input_dates = message.text.split()
        from_date = input_dates[1] if len(input_dates) > 1 else '01-Jan-1970'
        to_date = input_dates[2] if len(input_dates) > 2 else '31-Dec-2070'

        from_date = datetime.strptime(from_date, "%d-%b-%Y")
        to_date = datetime.strptime(to_date, "%d-%b-%Y")

        message = "Alright. Compiling your expense history in a pdf file!"
        bot.send_message(chat_id, message)
        
        fig = display_pie_chart(user_history, user_budget, from_date, to_date)

        # Save the figure as a PDF
        fig.savefig("expense_history.pdf")
        plt.close(fig)
        
        # Send the PDF document
        bot.send_document(chat_id, open("expense_history.pdf", "rb"))
        message = "Done!"
        bot.send_message(chat_id, message)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops! " + str(e))
