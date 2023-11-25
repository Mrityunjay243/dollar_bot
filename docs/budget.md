# About MyDollarBot's /budget Feature
This feature enables the user to add, remove, edit or display a budget in their expense tracker. The user can choose between an overall expense tracker, which counts every expenses made to the budget, or a category-wise expense tracker, which only counts expenses in a particular category towards the budget for that category.

The user can choose a category and add the amount for the budget to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/budget.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the budget feature. It pop ups a menu on the bot asking the user to choose to add, remove or display a budget, after which control is given to post_operation_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. `post_operation_selection(message, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the budget.py file. Depending on the action chosen by the user, it passes on control to the corresponding functions which are all located in different files.   


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.
