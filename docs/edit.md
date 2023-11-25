# About MyDollarBot's /edit Feature
This feature enables the user to edit a previously entered expense in the app. The use can change the amount set in the bot with this command. 

Please note that this is still a Work In Progress.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/edit.py)

# Code Description
## Functions

1. `run(message, bot):`
This is the main function used to implement the delete feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It gets the details for the expense to be edited from here and passes control onto edit2(m, bot): for further processing.

2. `edit2(message, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the  run(message, bot): function in the same file. It validates the date provided by the user to see if it's been correctly entered. If not, it throws an error stating the date is incorrect. If the date is correct, it then asks the user what they would like to edit for the expense in question, passing on to edit3(m, bot): for further processing.

3. `edit3(message, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the   edit2(m, bot):: function in the same file. Based on the category chosen for editing by the user, it redirects to the corresponding function for further processing.

4. `edit_date(m, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the   edit3(m, bot):: function in the same file. It takes care of date change and edits.

5. `edit_cost(m, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the   edit3(m, bot):: function in the same file. It takes care of cost change and edits.

6. `edit_cat(m, bot):`
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the   edit3(m, bot):: function in the same file. It takes care of category change and edits.

# How to run this feature?
Sri Athithya Kruth, [20.10.21 20:33]
/edit
(WORK IN PROGRESS)
