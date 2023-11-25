# About MyDollarBot's /pdf Feature
This feature enables the user to export all the expenses either from the start or for a given time period. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/pdf.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the pdf feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper.py to get the user's historical data and based on whether there is data available, it either prints an error message or displays the user's historical data.

2. `display_pie_chart(user_history, user_budget, from_date, to_date):`
This is the function which prints out the pie chart on the pdf document based on different categories. It takes **user_history**, **user_budget**, **from_date**, and **to_date** as inputs. Last two parameters are optional and if not provided will consider complete history to generate pie chart.

3. `calculate_expenses_by_category(user_history, from_date, to_date):`
This function calculates the budget based on the different categories and it requires **user_history**, **from_date**, and *&**to_date** as inputs. Last two parameters are optional and if not provided will consider complete history to calculate expenses by category.

4. `is_overall_budget_exceeded(user_history, overall_budget):`
As the name suggests this function checks whether the user has exceeded the overall budget specified or not. It requires **user_history**, and **overall_budget** as input parameters.

5. `calculate_total_expenses(user_history):`
This function simply calculates the total expenses.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.