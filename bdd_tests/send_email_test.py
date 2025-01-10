"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
from pytest_bdd import scenarios, given, when, then, parsers

from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail
from src.json_file.json_file import JsonFile


scenarios("features/send_email.feature")

DIRECTORY_TO_SHARED_CREDENTIALS = "resources"
JSON_FILE_NAME = "shared_credentials.json"

credentials_and_password = JsonFile(directory=DIRECTORY_TO_SHARED_CREDENTIALS, file_name=JSON_FILE_NAME)


@given('Google\'s "Sign in" page is displayed, system will automatically login into account based on '
       'credentials from level 1')
def login_page_open(login: Login) -> None:
    """
    Step definition for automatic login into the Google account based on credentials from JSON file.

    :param shared_credentials: Empty dictionary.
    :param login: The instance of Login to perform login operations.
    """
    shared_credentials = credentials_and_password.read_json_file()
    login.execute_login(shared_credentials)


@when(parsers.parse(
    'the name "{name_from_contacts}" with email address "{email_address_from_contacts}" is picked up from contacts'))
def create_email(name_from_contacts: str, email_address_from_contacts: str,
                 send_the_email: SendEmail) -> None:
    """
    Step definition for creating an email with specific contact information.

    :param shared_credentials: A dictionary containing the email address.
    :param name_from_contacts: The name of the contact.
    :param email_address_from_contacts: The email address of the contact.
    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """
    credentials_and_password.update_to_json_file(data={"name_from_contacts": name_from_contacts,
                                                       "email_address_from_contacts": email_address_from_contacts})
    shared_credentials = credentials_and_password.read_json_file()
    send_the_email.prepare_email(shared_credentials)


@when('the email is prepared for attachement')
def prepare_email(send_the_email: SendEmail) -> None:
    """
    Step definition that the name_from_contacts and email_address_from_contacts are already given.

    :param shared_credentials: A dictionary containing the email address.
    :param send_the_email: The instance of SendEmail to perform send_email operations.
    """
    send_the_email.prepare_email_for_attachement()


@then('attach the file named as funny_picture.png')
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
def execute_logout(logout: Logout) -> None:
    """
    Step definition for executing the logout process.

    :param shared_credentials: A dictionary containing all keys.
    :param logout: The instance of Logout to perform logout operations.
    """
    shared_credentials = credentials_and_password.read_json_file()
    logout.execute_logout(shared_credentials)
