import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from src.login import Login
from src.logout import Logout
from src.get_password import bdd_get_password_from_env
from src.json_shared_credentials import update_shared_credentials


scenarios("features/login_logout.feature")


@pytest.fixture(scope="session")
def shared_credentials() -> dict:
    """
    Fixture for creating the dictionary which will be used for whole session.

    :return: Empty dictionary for shared credentials.
    """
    return {}


@given('Google\'s \"Sign in\" page is displayed by FireFox web browser')
def login_page_open() -> None:
    """
    Step definition for opening Google's "Sign in" page.

    This step does not require any specific action as it's just a precondition for the scenario and the setup is
    made in conftest.py.
    """
    pass


@when(parsers.parse('the login name is filled out with the email address "{email}"'))
def fill_user_name(shared_credentials: dict, email: str) -> None:
    """
    Step definition for filling out the login name with an email address.

    :param shared_credentials: A dictionary which will be used for whole session.
    :param email: The email address to be filled in.
    """
    shared_credentials["email"] = email


@when('the password on the second page is populated using the password stored in the \"config.env\" file')
def fill_password(shared_credentials: dict) -> None:
    """
    Step definition for filling out the password on the second page from the "config.env" file.

    :param shared_credentials: A dictionary dedicated for whole session containing the email address.
    """
    shared_credentials["password"] = bdd_get_password_from_env()


@then('execute the login into the email')
def execute_login(shared_credentials: dict, login: Login) -> None:
    """
    Step definition for executing the login into the email account.

    :param shared_credentials: A dictionary dedicated for whole session containing 'email' and 'password'.
    :param login: The instance of Login to perform login operations.
    """
    login.execute_login(shared_credentials)


@when(parsers.parse('the user clicks the Google account with the name "{account_name}"'))
def google_account(shared_credentials: dict, account_name: str) -> None:
    """
    Step definition for clicking on a Google account and then logging out, also update credentials into JSON file for
    the future use.

    :param shared_credentials: A dictionary dedicated for whole session containing 'account_name'.
    :param account_name: The name of the Google account.
    """
    shared_credentials["account_name"] = account_name
    update_shared_credentials(shared_credentials)


@then(parsers.parse('execute logout'))
def execute_logout(shared_credentials: dict, logout: Logout) -> None:
    """
    Step definition for executing the logout process.

    :param shared_credentials: A dictionary dedicated for whole session containing 'account_name'.
    :param logout: The instance of Logout to perform logout operations.
    """
    logout.execute_logout(shared_credentials)
