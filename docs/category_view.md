# About MyDollarBot's /category Feature
This feature enables the user to view the list of categories.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/category_view.py)

# Code Description
## Functions

1. `run(message, bot):`
This function is designed to respond to a user's message in a Telegram bot. It does the following:
It calls helper.read_json(), which presumably reads data from a JSON file. This action may be related to loading or updating data related to spending categories.
It creates a one-time reply keyboard markup using types.ReplyKeyboardMarkup with a row width of 2. This markup is used to create response options for the user.
It retrieves the chat_id from the message object. This is necessary to know where to send the response.
It calls helper.getSpendCategories() to get a list of spending categories from the helper module.
It checks if there are categories available:
If there are categories in the list, it creates a message listing each category with bullet points and sends it as a response to the user.
If there are no categories available, it sends a message indicating that there are no categories to display.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /category and select view from the provided options.
