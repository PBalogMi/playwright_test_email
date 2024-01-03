# From Python to Pytest BDD thanks to Playwright and Gherkin

## Description

This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright. The project is divided into two sections:
- [BASIC BDD TESTS](#basic-bdd-tests) 
- [ADVANCED BDD TESTS](#advanced-bdd-tests)

In today's market, the demand for APP testing also encompasses the Robot Framework. You can explore an example here:
- [BONUS ROBOT FRAMEWORK](#bonus-robot-framework)


## Prerequisites

Before running the case study, ensure you have the following tools installed:

- Python 3.10
- PyCharm Community Edition 2023.2.4 (or any other code editor)
- Linux (Ubuntu 22.04), or Windows (optional with WSL)
- Firefox Browser (Version 119.0.1, 64-bit)

## Getting Started

1. Set up Gmail display language to English (US).

![Gmail Display Language Configuration](/files/gmail_setup/gmail_display_language.png)

2. Clone repository playwright_test_email to your local machine.

3. Install the required dependencies.

## BASIC BDD TESTS

The primary goal was to establish a straightforward BDD testing environment. 
However, it comes with clear drawbacks: each Scenario Outline in 
the [block.feature](/basic_bdd_tests/email_tests/features/block.feature) file includes login/logout steps, and there's 
also the issue of opening/closing a web page each time.

1. In the [block.feature](/basic_bdd_tests/email_tests/features/block.feature) file, please fill out 'Examples:' tables 
   with Gmail credentials (email, account_name) and account information (name_from_contacts, 
   email_address_from_contacts) from contacts list where test email should be sent. The email account's password 
   needs to be entered in the [config.env](/config.env) file.

   ⚠️ **Warning: Protect Your Credentials**

   **Do not share credentials through any repository. Always ensure that before sharing your code or committing changes, 
   all credentials are removed from 'Examples:' tables within [block.feature](/basic_bdd_tests/email_tests/features/block.feature) 
   files and also from the [config.env](/config.env) file. 
   Protect your sensitive information and avoid sharing it inadvertently.**

   
   **Note: The optimal choice is to include your personal email account in the contacts and enter it into the 'Examples:' 
   tables to avoid sending unsolicited emails to someone else's account.**

2. Set up your PyCharm environment for pytest testing as shown in the provided image.

![PyCharm Configuration](/files/pycharm_setup/basic_bdd_setup.png)

3. Run the tests using PyCharm or from the command line with the command pytest.

![Terminal commands](/files/terminal_commands/terminal_commands_basic_bdd_setup.png)

## ADVANCED BDD TESTS

The issue within Basic BDD tests has been resolved by leveraging @pytest.fixture(scope="session") for dictionary sharing
across scenarios. Managing the opening and closing of web pages has been handled through [conftest.py](/advanced_bdd_tests/email_tests/conftest.py), 
alongside the initialization of essential classes from the 'src' folder. Moreover, the implementation of a JSON file 
facilitates the automatic transfer of credentials to subsequent features, enabling seamless login/logout functionality."

1. In the [*.feature](/advanced_bdd_tests/email_tests/features) files, please fill out 'Examples:' tables with Gmail 
   credentials (eamil, account_name) and account information (name_from_contacts, email_address_from_contacts)
   from contacts list where test email should be sent.  The email account's password 
   needs to be entered in the [config.env](/config.env) file.

   ⚠️ **Warning: Protect Your Credentials**

   **Do not share credentials through any repository. Always ensure that before sharing your code or committing changes, 
   all credentials are removed from 'Examples:' tables within feature files and also from [config.env](/config.env) file.
   Protect your sensitive information and avoid sharing it inadvertently.**
 
   **Note: The optimal choice is to include your personal email account in the contacts and enter it into the 'Examples:' 
   tables to avoid sending unsolicited emails to someone else's account.**

2. Set up your PyCharm environment for pytest testing as shown in the provided images.

![PyCharm Configuration](/files/pycharm_setup/pycharm_advanced_bdd_setup1.png)
![PyCharm Configuration](/files/pycharm_setup/pycharm_advanced_bdd_setup2.png)

3. Run the tests using PyCharm or from the command line with the command pytest.

![Terminal commands](/files/terminal_commands/terminal_commands_advanced_bdd_setup.png)

## Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. 
All contributions are welcome!

## License
This project is licensed under the MIT License.

## BONUS ROBOT FRAMEWORK

"Work in progress. The current code is solely for [login and logout](/robot_framework/block.robot) functionalities."