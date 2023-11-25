# About MyDollarBot's /export Feature
This feature enables the user to export all the expenses stored in either Excel format or CSV format.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/export.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the export feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper.py to get the user's historical data and based on whether there is data available, it either prints an error message or displays the user's historical data.

2. `export_to_excel(user_history, file_path):`
This function is called by the run function when the user specifies the data to be exported in excel format. This function reads the complete transaction history and then writes it to an excel file which the user has an option to download.

3. `export_to_csv(user_history, file_path):`
This function is called by the run function when the user specifies the data to be exported in csv format. This function reads the complete transaction history and then writes it to an csv file which the user has an option to download.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.