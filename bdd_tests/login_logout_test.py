"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
from pytest_bdd import scenarios, given, when, then, parsers

from src.login import Login
from src.logout import Logout
from src.json_file.json_file import JsonFile
from src.get_password import get_password_from_env


scenarios("features/login_logout.feature")

DIRECTORY_TO_SHARED_CREDENTIALS = "resources"
JSON_FILE_NAME = "shared_credentials.json"

credentials_and_password = JsonFile(directory=DIRECTORY_TO_SHARED_CREDENTIALS, file_name=JSON_FILE_NAME)

@given('Google\'s \"Sign in\" page is displayed by FireFox web browser')
def login_page_open() -> None:
    """
    Step definition for opening Google's "Sign in" page.

    This step does not require any specific action as it's just a precondition for the scenario and the setup is
    made in conftest.py.
    """


@when(parsers.parse('the login name is filled out with the email address "{email}"'))
def fill_user_name(email: str) -> None:
    """
    Step definition for filling out the login name with an email address.

    :param email: The email address to be filled in.
    """
    credentials_and_password.update_to_json_file(data={"email": email})


@when('the password on the second page is populated using the password stored in the \"config.env\" file')
def fill_password() -> None:
    """
    Step definition for filling out the password on the second page from the "config.env" file.
    """
    password = get_password_from_env()
    credentials_and_password.update_to_json_file(data={"password": password})


@then('execute the login into the email')
def execute_login_test(login: Login) -> None:
    """
    Step definition for executing the login into the email account.

    :param login: The instance of Login to perform login operations.
    """
    credentials = credentials_and_password.read_json_file()
    login.execute_login(credentials)


@when(parsers.parse('the user clicks the Google account with the name "{account_name}"'))
def google_account(account_name: str) -> None:
    """
    Step definition for clicking on a Google account and then logging out, also update credentials into JSON file for
    the future use.

    :param account_name: The name of the Google account.
    """
    credentials_and_password.update_to_json_file(data={"account_name": account_name})


@then('execute logout')
def execute_logout(logout: Logout) -> None:
    """
    Step definition for executing the logout process.

    :param logout: The instance of Logout to perform logout operations.
    """
    credentials = credentials_and_password.read_json_file()
    logout.execute_logout(credentials)
