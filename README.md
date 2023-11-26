# 💰 Expense Management Bot 💰

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#why-should-you-use-Dollar Bot">Why should you use Expense-Management-Bot?</a></li>
    <li><a href="#check-out-the-video">Check out the video!</a></li>
    <li><a href="#what-is-new-in-this-version">What is new in this version?</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#code-coverage">Code Coverage</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#code-documentation">Code Documentation</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
    <li><a href="#future-roadmap">Future RoadMap</a></li>
   <li><a href="#contributors">Contributors</a></li>
   <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<hr>
<p align="center">
<a><img  height=350 width=350 
  src="https://s1.mzstatic.com/us/r30/Purple1/v4/de/ab/45/deab454d-8881-b37d-9513-b0e26424cc57/pr_source.png?downloadKey=1425248837_8a393efcc4a821cbf9639d5570f8e966" alt="Dollar BoT"></a>
</p>
<hr>

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Mrityunjay243/dollar_bot)

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/sak007/MyDollarBot-BOTGo)](https://github.com/Mrityunjay243/dollar_bot/graphs/contributors)
[![DOI](https://zenodo.org/badge/706356133.svg)](https://zenodo.org/doi/10.5281/zenodo.10019963)
[![Build Status](https://app.travis-ci.com/usmanwardag/dollar_bot.svg?branch=main)](https://app.travis-ci.com/usmanwardag/dollar_bot)
[![codecov](https://codecov.io/gh/usmanwardag/dollar_bot/branch/main/graph/badge.svg?token=PYAWX95R67)](https://codecov.io/gh/usmanwardag/dollar_bot)

[![GitHub issues](https://img.shields.io/github/issues/Mrityunjay243/dollar_bot)](https://github.com/Mrityunjay243/dollar_bot/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/Mrityunjay243/dollar_bot)](https://github.com/Mrityunjay243/dollar_bot/issues?q=is%3Aissue+is%3Aclosed)

<hr>

## Why should you use Expense Management Bot?

Dollar Bot is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  
With simple commands, this bot allows you to:
- Add/Record new spendings
- Display your spendings through bar graph
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to

## Check out the video!

[![Demo Video](https://i9.ytimg.com/vi/aCjcT1CHAzU/mq3.jpg?sqp=COSotI0G&rs=AOn4CLD34jFIlq6GRdmTnK6p3F8O2F-Yig)](https://www.youtube.com/watch?v=O0sEIM39ejE)

## What is new in this version?

Checkout the [this documentation](https://github.com/ebanigogia/dollar_bot/blob/main/What_is_new.pdf)
## Installation

The below instructions can be followed in order to set-up this bot at your end in a span of few minutes! Let's get started:

1. Clone this repository to your local system.

2. Start a terminal session in the directory where the project has been cloned. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt

```
3. Download and install the Telegram desktop application for your system from the following site:
 ```
 https://desktop.telegram.org/
 ```
## How to run?

1. In Telegram, search for "BotFather". Click on "Start", and enter the following command:
```
  /newbot
```
2. Follow the instructions on screen and choose a name for your bot (e.g., `dollarbot`). After this, select a username for your bot that ends with "bot". The username has to be unique. 

3. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use.

4. In the repo directory (where you cloned it), run these commands to (i) grant execution access to a bash script, and (ii) execute that bash script to run the Telegram Bot (make sure that you use a UNIX based CLI to run the shell files):
```
   chmod a+x run_tele.sh
   ./run_tele.sh
```
   
(OR)
```
   chmod a+x run_tele.sh
   bash run_tele.sh
```
```Note```: It will ask you to paste the API token you received from Telegram in step 4.
A successful run will generate a message on your terminal that says "TeleBot: Started polling." 

5. In the Telegram app, search for your newly created bot by entering the username and open the same. Now, on Telegram, enter the "/start" or "menu" command, and you are all set to track your expenses!

### Run Automatically at Startup

To run the script automatically at startup / reboot, simply add the `.run_forever.sh` script to your `.bashrc` file, which executes whenever you reboot your system.

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:
```
python run -m pytest test/
```

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

## License

This project is licensed under the terms of the MIT license. Please check [License](https://github.com/Mrityunjay243/dollar_bot/blob/main/LICENSE) for more details.


## Code Documentation

Checkout the [docs](https://github.com/sak007/MyDollarBot-BOTGo/tree/main/docs)

## How to Contribute

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/Mrityunjay243/dollar_bot/blob/main/CONTRIBUTING.md)

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/Mrityunjay243/dollar_bot/issues).

## Future RoadMap

- The bot can be integrated with Slack like it is currently done with discord to make it seamless to use. 
- More content can be added for the way notifications can be displayed on the user front. This can be done to make the UI more interactive.

## Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/Mrityunjay243"><br /><sub><b>Mrityunjay Joshi</b></sub></a></td>
    <td align="center"><a href="https://github.com/AtharvaThorve"><br /><sub><b>Atharva Thorve</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/divitkalathil"><br /><sub><b>Divit Kalathil</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/raghavnarula"><br /><sub><b>Raghav Narula</b></sub></a><br /></td>
  </tr>
</table>

## Chat Channel

- https://discord.gg/vStKkEEA

## Acknowledgements

- We would like to express our gratitude 🙏🏻 and a big thank you 😇 to Prof. Dr. Timothy Menzie for giving us the opportunity to get into the shoes of software building and learning new skills and development process throught the project building.
- A big thank you 😊 to the Teaching Assistants for their support.
- Thank you to the previous team 😊 for a thorough ReadMe and deatiled documentation.[ExpenseManagementBot](https://github.com/Mrityunjay243/dollar_bot/blob/main/README.md)
- Thank you to the ⭐️[Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot)




