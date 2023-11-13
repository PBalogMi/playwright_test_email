# From Python to Pytest BDD thanks to Playwright and Gherkin

## Description

This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.

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

4. In the 'block.feature' file, please fill out 'Examples:' tables with Gmail credentials (eamil, password, account_name) and
   account information (name_from_contacts, email_address_from_contacts) from contacts list where test email should be sent.
   
   **Note: The optimal choice is to include your personal email account in the contacts and enter it into the 'Examples:' 
   tables to avoid sending unsolicited emails to someone else's account.**

5. Set up your PyCharm environment for pytest testing as shown in the provided image.

![PyCharm Configuration](/files/pycharm_setup/pycharm_pytest_setup.png)

6. Run the tests using PyCharm or from the command line with the command pytest.

## Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. 
All contributions are welcome!

## License
This project is licensed under the MIT License.