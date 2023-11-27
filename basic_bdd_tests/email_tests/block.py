from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail


scenarios("features/block.feature")


@given('Google\'s \"Sign in\" page is displayed')
def login_page_open() -> None:
    """
    Step definition for opening Google's "Sign in" page.

    This step does not require any specific action as it's just a precondition for the scenario and the setup is
    made in conftest.py.
    """
    pass


@when(parsers.parse('the login name is filled out with the email address "{email}"'),
      target_fixture="credentials")
def fill_user_name(email: str) -> dict:
    """
    Step definition for filling out the login name with an email address.

    :param email: The email address to be filled in.
    :return: A dictionary containing the email address.
    """
    return {"email": email}


@when(parsers.parse('the password on the second page is filled out with "{password}"'))
def fill_password(credentials: dict, password: str) -> None:
    """
    Step definition for filling out the password on the second page.

    :param credentials: A dictionary containing the email address.
    :param password: The password to be filled in.
    """
    credentials["password"] = password


@then('execute the login into the email')
def execute_login(credentials: dict, main_page: Page) -> None:
    """
    Step definition for executing the login into the email account.

    :param credentials: A dictionary containing 'email' and 'password'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_execute_login = Login(main_page)
    call_execute_login.execute_login(credentials)


@when(parsers.parse(
    'pick up the name "{name_from_contacts}" with email address "{email_address_from_contacts}" from contacts'))
def create_email(credentials: dict, name_from_contacts: str, email_address_from_contacts: str) -> None:
    """
    Step definition for creating an email with specific contact information.

    :param credentials: A dictionary containing the email address.
    :param name_from_contacts: The name of the contact.
    :param email_address_from_contacts: The email address of the contact.
    """
    credentials["name_from_contacts"] = name_from_contacts
    credentials["email_address_from_contacts"] = email_address_from_contacts


@then('attach file named as funny_picture.png')
def attach_file(main_page: Page) -> None:
    """
    Step definition for attaching a file named "funny_picture.png" to the email.

    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_send_email = SendEmail(main_page)
    call_send_email.add_attachment()


@then('send an email with an attached file named funny_picture.png')
def prepare_email(credentials: dict, main_page: Page) -> None:
    """
    Step definition for preparing an email with an attached file.

    :param credentials: A dictionary containing 'email', 'name_from_contacts', and 'email_address_from_contacts'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_prepare_email = SendEmail(main_page)
    call_prepare_email.prepare_email(credentials)
    call_prepare_email.add_attachment()
    call_prepare_email.send_email()


@then('send email')
def send_email(credentials: dict, main_page: Page) -> None:
    """
    Step definition for sending an email.

    :param credentials: A dictionary containing 'email', 'name_from_contacts', and 'email_address_from_contacts'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_send_email = SendEmail(main_page)
    call_send_email.prepare_email(credentials)
    call_send_email.send_email()


@when(parsers.parse('the user clicks Google account labeled "{account_name}"'))
def google_account(credentials: dict, account_name: str) -> None:
    """
    Step definition for clicking on a Google account.

    :param credentials: A dictionary containing 'account_name'.
    :param account_name: The name of the Google account.
    """
    credentials["account_name"] = account_name


@then(parsers.parse('the user clicks the logout button'))
def execute_logout(credentials: dict, main_page: Page):
    """
    Step definition for executing the logout process.

    :param credentials: A dictionary containing 'account_name'.
    :param main_page: An instance of a Playwright Page object representing the current browser page.
    """
    call_execute_logout = Logout(main_page)
    call_execute_logout.execute_logout(credentials)
