# About MyDollarBot's /search Feature
This feature enables the user to view all of their stored records for a specific search category i.e it gives a historical view of all the expenses of a specific category stored in the DollarBot.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/search.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the search feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It displays a menu of categories that already exists in the **bot** and prompts user to select one of them.

2. `post_select_category(message, bot):`
This is the function which is called after the user selects a category. We first read the whole history and then filter out the entries which do not correspond to the **category** selected by the user.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /search into the telegram bot.