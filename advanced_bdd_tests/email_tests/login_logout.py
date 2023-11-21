import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

from src.json_shared_credentials import update_shared_credentials
from src.login import Login
from src.logout import Logout

scenarios("features/login_logout.feature")


@pytest.fixture(scope="session")
def shared_credentials() -> dict:
    """
    Fixture for creating the dictionary which will be used for whole session.

    :return: Empty dictionary
    """
    return {}


@given('Google\'s \"Sign in\" page is displayed by FireFox web browser')
def login_page_open() -> None:
    """
    Step definition for opening Google's "Sign in" page.

    This step does not require any specific action as it's just a precondition for the scenario.
    """
    pass


@when(parsers.parse('the login name is filled out with the email address "{email}"'))
def fill_user_name(shared_credentials: dict, email: str) -> None:
    """
    Step definition for filling out the login name with an email address.

    :param shared_credentials: A dictionary which will be used for whole session.
    :param email: The email address to be filled in.
    :return: A dictionary containing the email address.
    """
    shared_credentials["email"] = email
    update_shared_credentials(shared_credentials)


@then(parsers.parse('the password on the second page is filled out with "{password}"'))
def fill_password(shared_credentials: dict, password: str) -> None:
    """
    Step definition for filling out the password on the second page.

    :param shared_credentials: A dictionary dedicated for whole session containing the email address.
    :param password: The password to be filled in.
    """
    shared_credentials["password"] = password
    update_shared_credentials(shared_credentials)


@then('execute the login into the email')
def execute_login(shared_credentials: dict, main_page: Page) -> None:
    """
    Step definition for executing the login into the email account.

    :param shared_credentials: A dictionary dedicated for whole session containing 'email' and 'password'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_execute_login = Login(main_page)
    call_execute_login.execute_login(shared_credentials)


@when(parsers.parse('the user clicks the Google account with the name "{account_name}" and then the logout button'))
def google_account(shared_credentials: dict, account_name: str) -> None:
    """
    Step definition for clicking on a Google account and then logging out.

    :param shared_credentials: A dictionary dedicated for whole session containing 'account_name'.
    :param account_name: The name of the Google account.
    """
    shared_credentials["account_name"] = account_name
    update_shared_credentials(shared_credentials)


@then(parsers.parse('execute logout'))
def execute_logout(shared_credentials: dict, main_page: Page) -> None:
    """
    Step definition for executing the logout process.

    :param shared_credentials: A dictionary dedicated for whole session containing 'account_name'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_execute_logout = Logout(main_page)
    call_execute_logout.execute_logout(shared_credentials)