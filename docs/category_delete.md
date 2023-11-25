# About MyDollarBot's /category Feature
This feature enables the user to delete the category from the list.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/category_delete.py)

# Code Description
## Functions

1. `run(message, bot):`
This function is called when the user initiates the process of deleting a spending category. It does the following:
Calls helper.read_json(), presumably to read data from a JSON file that may contain information about spending categories.
Retrieves the chat_id from the message object, which is necessary to know where to send responses.
Sends a message to the user, asking them which category they want to delete.
Registers a "next step handler," which will be deletion, to handle the user's response. It also passes the bot object as an argument to the next step handler.

2. `deletion(message, bot):`
This function is called after the user provides the category they want to delete. It performs the following tasks:
Creates a one-time reply keyboard markup.
Retrieves the chat_id from the message object.
Retrieves the category to be removed from the user's message.
Converts the user's input to lowercase and compares it with lowercase versions of categories obtained from helper.getSpendCategories().
If the category to remove is found in the list of categories, it asks the user for confirmation by sending a message with "Y/N" options.
If the category is not in the list, it informs the user that the category is not in the list.

3. `confirm_deletion(message, bot, category_to_remove):`
This function handles the user's confirmation to delete a category. It does the following:
Retrieves the chat_id from the message object.
Gets the user's response (either "Y" or "N").
If the user's response is "Y" (indicating confirmation to delete), it checks if the category to remove is in the list of categories. If found, it removes the category using helper.getSpendCategories().remove(category_to_remove) and sends a confirmation message. If not found, it informs the user that the category was not in the list.
If the user's response is "N" (indicating cancellation), it informs the user that the deletion has been canceled.
If the user's response is neither "Y" nor "N," it informs the user that their response is invalid and asks for "Y" or "N."

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /category and select delete from the given options.
