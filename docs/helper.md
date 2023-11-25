# About MyDollarBot's /helper class
The helper file contains a set of functions that are commonly used for repeated tasks in the various features of MyDollarBot. Since these come up often, we have put them all up here in a separate file for reusability.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/helper.py)

# Code Description
## Functions

1. `read_json():`
Function to load .json expense record data

2. `write_json(user_list):`
Stores data into the datastore of the bot.

3. `validate_entered_amount(amount_entered):`
Takes 1 argument, **amount_entered**. It validates this amount's format to see if it has been correctly entered by the user.

4. `getUserHistory(chat_id):`
Takes 1 argument **chat_id** and uses this to get the relevant user's historical data.

5. `getSpendCategories():`
This functions returns the spend categories used in the bot. These are defined the same file.

6. `getSpendDisplayOptions():`
This functions returns the spend display options used in the bot. These are defined the same file.

7. `getCommands():`
This functions returns the command options used in the bot. These are defined the same file.

8. `getDateFormat():`
This functions returns the date format used in the bot. 

9. `getTimeFormat():`
This functions returns the time format used in the bot. 

10. `getMonthFormat():`
This functions returns the month format used in the bot. 

11. `convertCurrency(amount, from_currency):`
This function converts the amount entered from the *from_currency* specified to *USD*.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

This file is not a feature and cannot be run per se. Its functions are used all over by the other files as it provides helper functions for various functionalities and features.