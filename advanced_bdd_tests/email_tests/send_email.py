import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail
from src.json_shared_credentials import read_shared_credentials
from src.json_important_keys import check_json_keys
from src.custom_exceptions import MissingDataError


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
def login_page_open(shared_credentials: dict, login: Login) -> None:
    """
    Step definition for automatic login into the Google account based on credentials from JSON file.

    :param shared_credentials: Empty dictionary.
    :param login: The instance of Login to perform login operations.
    """

    shared_credentials_from_json_file = read_shared_credentials()
    check_json_file = check_json_keys()
    if check_json_file:
        raise MissingDataError
    shared_credentials.update(shared_credentials_from_json_file)  # transfer credential from login_logout.py test
    login.execute_login(shared_credentials)


@when('you are already logged in the Google account')
def already_logged_in() -> None:
    """
    Step definition that the user is already logged in the Google account.

    This step does not require any specific action as it's just a condition for the scenario.
    """


@when(parsers.parse(
    'the name "{name_from_contacts}" with email address "{email_address_from_contacts}" is picked up from contacts'))
def create_email(shared_credentials: dict, name_from_contacts: str, email_address_from_contacts: str,
                 send_the_email: SendEmail) -> None:
    """
    Step definition for creating an email with specific contact information.

    :param shared_credentials: A dictionary containing the email address.
    :param name_from_contacts: The name of the contact.
    :param email_address_from_contacts: The email address of the contact.
    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """
    shared_credentials["name_from_contacts"] = name_from_contacts
    shared_credentials["email_address_from_contacts"] = email_address_from_contacts
    send_the_email.prepare_email(shared_credentials)


@when('the name and email address from contacts are already given from level 2 - Examples table')
def attach_file(shared_credentials: dict, send_the_email: SendEmail) -> None:
    """
    Step definition that the name_from_contacts and email_address_from_contacts are already given.

    :param shared_credentials: A dictionary containing the email address.
    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """
    send_the_email.prepare_email(shared_credentials)


@then('attach file named as funny_picture.png')
def attach_file(send_the_email: SendEmail) -> None:
    """
    Step definition for attaching a file named "funny_picture.png" to the email.

    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """
    send_the_email.add_attachment()


@then('send email')
def send_email(send_the_email: SendEmail) -> None:
    """
    Step definition for sending an email.

    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """

    send_the_email.send_email()


@then('the user clicks the Google account with the account name from level 1 and then the logout button')
def execute_logout(shared_credentials: dict, logout: Logout):
    """
    Step definition for executing the logout process.

    :param shared_credentials: A dictionary containing all keys.
    :param logout: The instance of Logout to perform logout operations.
    """
    logout.execute_logout(shared_credentials)
