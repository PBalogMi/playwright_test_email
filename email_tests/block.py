from pytest_bdd import scenarios, given, when, then, parsers
from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail


scenarios("features/block.feature")


@given('the Google\'s \"Sign in\" page is displayed')
def login_page_open():
    pass


@when(parsers.parse('the login name is filled out with email address "{email}"'),
      target_fixture="credentials")
def fill_user_name(email):
    return {"email": email}


@then(parsers.parse('the password on the second page is filled out with "{password}"'))
def fill_password(credentials, password):
    credentials["password"] = password


@then('execute the login into email')
def execute_login(credentials, main_page):
    call_execute_login = Login(main_page)
    call_execute_login.execute_login(credentials)


@then(parsers.parse(
    'pick up the name "{name_from_contacts}" with email address "{email_address_from_contacts}" from contacts'))
def create_email(credentials, name_from_contacts, email_address_from_contacts):
    credentials["name_from_contacts"] = name_from_contacts
    credentials["email_address_from_contacts"] = email_address_from_contacts


@then('attach file named as funny_picture.png')
def attach_file(main_page):
    call_send_email = SendEmail(main_page)
    call_send_email.add_attachment()


@then('prepare email')
def prepare_email(credentials, main_page):
    call_prepare_email = SendEmail(main_page)
    call_prepare_email.prepare_email(credentials)


@then('send email')
def send_email(main_page):
    call_send_email = SendEmail(main_page)
    call_send_email.send_email()


@then(parsers.parse('the user click Google account with name "{account_name}" and then logout button'))
def google_account(credentials, account_name):
    credentials["account_name"] = account_name


@then(parsers.parse('execute logout'))
def execute_logout(credentials, main_page):
    call_execute_logout = Logout(main_page)
    call_execute_logout.execute_logout(credentials)
