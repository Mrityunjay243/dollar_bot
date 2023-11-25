# About MyDollarBot's /display Feature's Graph module
This feature enables the user to see their expense in a graphical format to enable better UX.

Currently, the /display command will provide the expenses as a message to the users via the bot. To better the UX, we decided to add the option to show the expenses in a Bar Graph.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/Mrityunjay243/dollar_bot/blob/main/code/graphing.py)

# Code Description
## Functions

1. `visualize(total_text):`
This is the main function used to implement the graphing part of display feature. This file is called from display.py, and takes the user expense as a string and creates a dictionary which in turn is fed as input matplotlib to create the graph

2. `addlabels(x, y):`
This function is used to add the labels to the graph. It takes the expense values and adds the values inside the bar graph for each expense type

# How to run this feature?
After you've added sufficient input data, use the /display command and you can see the output in a pictorial representation. 
