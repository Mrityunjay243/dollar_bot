# About MyDollarBot's /expense Feature
This feature enables the user to add/update/delete their expense in a pre-existing category.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/ebanigogia/dollar_bot/blob/main/code/expense.py)

# Code Description
## Functions

1. `process_expense_command` Function:
This function handles the initial expense-related command from a user.
It sends a message to the user with a keyboard markup that allows them to choose from options: "Add," "Delete," or "Update."
It registers a callback function (expense_option_selection) to handle the user's choice.

2. `expense_option_selection` Function:
This function is called when the user selects an option from the keyboard markup.
Depending on the selected option ("Add," "Delete," or "Update"), it directs the user to the respective function to perform that action.

3. `select_expense_category` Function:
This function is used to select the category for an expense.
It sends a message with a keyboard markup containing expense categories.
It registers a callback function (expense_category_selected) to handle the user's category selection.

4. `expense_category_selected` Function:
This function processes the selected expense category.
It validates the selected category and asks the user for the amount spent in that category.
It registers a callback function (record_expense) to handle the amount of input.

5. `record_expense` Function:
This function records the expense with the specified category and amount.
It validates the amount, checks if it's nonzero, and records the expense along with the current date and time.
It then stores the expense in the user's data and sends a confirmation message.
Finally, it calls helper.display_remaining_budget to display the remaining budget information for the category.

6. `delete_expense` Function:
This function allows the user to select an expense to delete.
It retrieves the user's expense history, generates a keyboard markup with the expenses, and registers a callback to confirm the deletion.

7. `confirm_delete_expense` Function:
This function confirms and deletes the selected expense.
It updates the user's data by removing the selected expense and writes the updated data back to storage.
It then sends a confirmation message and calls helper.display_remaining_budget to display the remaining budget information.

8. `add_user_record` Function:
This function is used to add a new record to the user's data.
It takes the user's chat ID and the record to be added, updates the user's data, and returns the updated data

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /expense into the telegram bot.

