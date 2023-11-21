import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

from src.json_shared_credentials import read_shared_credentials
from src.json_important_keys import check_json_keys
from src.custom_exceptions import MissingDataError
from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail

scenarios("features/send_email.feature")


@pytest.fixture(scope="session")
def shared_credentials() -> dict:
    """
    Fixture for creating the dictionary which will be used for whole session.

    :return: Empty dictionary
    """
    return {}


@given('Google\'s "Sign in" page is displayed, system will automatically login into account based on '
       'credentials from level 1')
def login_page_open(main_page: Page) -> None:
    """
    Step definition for login into the Google account and creating target_fixture.
    This step does not require any specific action as it's just a condition for scenarios.

    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """

    shared_credentials_from_json_file = read_shared_credentials()
    check_json_file = check_json_keys()
    if check_json_file:
        raise MissingDataError

    call_execute_login = Login(main_page)
    call_execute_login.execute_login(shared_credentials_from_json_file)


@when('you are already logged in the Google account')
def already_logged_in() -> None:
    """
    Step definition that the user is already logged in the Google account.

    This step does not require any specific action as it's just a condition for the scenario.
    """


@then(parsers.parse(
    'pick up the name "{name_from_contacts}" with email address "{email_address_from_contacts}" from contacts'))
def create_email(shared_credentials: dict, name_from_contacts: str, email_address_from_contacts: str) -> None:
    """
    Step definition for creating an email with specific contact information.

    :param shared_credentials: A dictionary containing the email address.
    :param name_from_contacts: The name of the contact.
    :param email_address_from_contacts: The email address of the contact.
    """
    shared_credentials["name_from_contacts"] = name_from_contacts
    shared_credentials["email_address_from_contacts"] = email_address_from_contacts


@then('pick up the name and email address from contacts which were already given from level 2 - Examples table')
def attach_file() -> None:
    """
    Step definition that the name_from_contacts and email_address_from_contacts are already given.

    This step does not require any specific action as it's just a condition for the scenario.
    """


@then('attach file named as funny_picture.png')
def attach_file(main_page: Page) -> None:
    """
    Step definition for attaching a file named "funny_picture.png" to the email.

    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_send_email = SendEmail(main_page)
    call_send_email.add_attachment()


@then('attach file named as funny_picture.png and send email')
def attach_file_and_send_email(shared_credentials: dict, main_page: Page) -> None:
    """
    Step definition for preparing an email with an attached file.

    :param shared_credentials: A dictionary containing 'email', 'name_from_contacts', and 'email_address_from_contacts'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_prepare_email = SendEmail(main_page, shared_credentials)
    call_prepare_email.prepare_email()
    call_prepare_email.add_attachment()
    call_prepare_email.send_email()


@then('send email')
def send_email(shared_credentials: dict, main_page: Page) -> None:
    """
    Step definition for sending an email.

    :param shared_credentials: A dictionary containing 'email', 'name_from_contacts', and 'email_address_from_contacts'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_send_email = SendEmail(main_page, shared_credentials)
    call_send_email.prepare_email()
    call_send_email.send_email()


@then('the user clicks the Google account with the account name from level 1 and then the logout button')
def execute_logout(main_page: Page):
    """
    Step definition for executing the logout process.

    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_execute_logout = Logout(main_page)
    shared_credentials_from_json_file = read_shared_credentials()
    call_execute_logout.execute_logout(shared_credentials_from_json_file)
