import os
from playwright.sync_api import Page


class SendEmail:
    """
    Class for sending an email using provided credentials.
    """

    def __init__(self, page: Page):
        """
        Initialize the SendEmail object.

        :param page: An instance of a Playwright Page object representing the current browser page.
        """
        self.page = page
        self._name_io = None

    def iframe_name_io(self) -> None:
        """
        Extracts the id and the 'name' attribute of the open iframe with the expected state 'Contacts'.

        :return: None
        """
        try:
            # Extract id and the 'name' attribute
            # Condition: expected state iframe "Contacts" is already open
            iframe_element = self.page.locator('iframe[id^="I0_"]').first
            self._name_io = iframe_element.get_attribute('name')
        except Exception as e:
            print(f'It looks like iframe named "Contacts" is closed. '
                  f'Iframe "Contacts" will be opened and the testing will continue {e}')

        finally:
            if self._name_io is None:
                self.page.get_by_label("Contacts").locator("div").nth(2).click()
                iframe_element = self.page.locator('iframe[id^="I0_"]').first
                self._name_io = iframe_element.get_attribute('name')

    def prepare_email(self, credentials: dict) -> None:
        """
        Prepares an email by navigating through the iframe and filling out the email details.

        :param credentials: A dictionary containing 'name_from_contacts' and 'email_address_from_contacts'.
                            'name_from_contacts': The name associated with the contact.
                            'email_address_from_contacts': The email address associated with the contact.

        :return: None
        """
        self.iframe_name_io()

        # check if the iframe for single contact is open
        # when the test continues without closing the web, single contact stays opened which causes test failure
        single_contact_iframe = (self.page.frame_locator(f"iframe[name=\"{self._name_io}\"]").locator(".ktSsrf").
                                 is_visible())
        if single_contact_iframe is False:
            self.page.frame_locator(f"iframe[name=\"{self._name_io}\"]"
                                    ).get_by_label(f"Name: {credentials['name_from_contacts']},"
                                                   f" Subtext: {credentials['email_address_from_contacts']}").click()
        self.page.frame_locator(f"iframe[name=\"{self._name_io}\"]").get_by_label("Send email").click()
        self.page.get_by_placeholder("Subject").fill("test")
        self.page.get_by_role("textbox", name="Message Body").fill("test\n")

    def add_attachment(self) -> None:
        """
        Adds an attachment to the email.

        :return: None
        """
        working_directory = os.getcwd()
        path_to_file = os.path.join(working_directory, 'files/attachment/funny_picture.png')

        with self.page.expect_file_chooser() as paper_clip:
            file_input = self.page.get_by_label("Attach files")
            file_input.click()
            file_chooser = paper_clip.value
            file_chooser.set_files(path_to_file)

    def send_email(self) -> None:
        """
        Sends the email.

        :return: None
        """
        self.page.get_by_label("Send ‪(Ctrl-Enter)‬").click()
