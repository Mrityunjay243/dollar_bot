# About MyDollarBot's /category Feature
This feature enables the user to add category in the list.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/category_add.py)

# Code Description
## Functions

1. `run(message, bot):`
This function is responsible for initiating the process of adding a new category for tracking expenses through a Telegram bot. It does the following:
Calls helper.read_json() to read some data (presumably related to categories or expenses).
Retrieves the user's chat_id from the message object.
Creates a reply keyboard markup for the user's response.
Sends a message to the user, asking if they want to add a new category ("Y/N").
Registers a "next step handler," which will be post_user_def_category, to handle the user's response. It also passes the bot object as an argument to the next step handler.

2. `post_user_def_category(message, bot):`
This function is called when the user responds with "Y" or "y" to the question of whether they want to add a new category. It does the following:
Creates another reply keyboard markup.
Retrieves the user's chat_id from the message object.
If the user responds with "Y" or "y," it sends a message to the user, asking them to enter a category.
Registers a "next step handler," which will be post_append_spend, to handle the user's response. It also passes the bot object as an argument to the next step handler.

3. `post_append_spend(message, bot):`
This function is called after the user enters a category they want to add. It handles the addition of the category to a list. Here's what it does:
Creates another reply keyboard markup.
Retrieves the selected category from the user's message.
Retrieves the user's chat_id from the message object.
Converts the user's input to lowercase for case-insensitive comparisons.
Retrieves a list of existing categories from the helper.getSpendCategories() function.
Checks if the entered category is already in the list of existing categories.
If the category is not already in the list, it adds the category to the list using helper.spend_categories.append(selected_category) and sends a message confirming the addition.
If the category is already in the list, it sends a message indicating that it won't be added again.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /category into the telegram bot and then select Add/Update option.
