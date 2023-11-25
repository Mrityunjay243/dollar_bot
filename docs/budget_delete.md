# About MyDollarBot's budget_delete module
The budget_view module contains all the functions required to implement the display delete/removal feature. In essence, all operations involved in removal and deletion of a budget are taken care of in this module and are implemented here. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/budget_delete.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the budget delete feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It gets the user's chat ID from the message object, and reads all user data through the read_json method from the helper module. It then proceeds to empty the budget data for the particular user based on the user ID provided from the UI. It returns a simple message indicating that this operation has been done to the UI.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Add a budget and then type /budget again. Please choose the option for deleting a budget.
