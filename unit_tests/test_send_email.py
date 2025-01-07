"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import unittest
import os
from unittest.mock import Mock
from playwright.sync_api import Page
from src.send_email import SendEmail


class TestSendEmail(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Page object from Playwright
        self.mocked_page = Mock(spec=Page)

        # Initialize SendEmail object with the Page object
        self.send_email = SendEmail(self.mocked_page)

    def test_iframe_name_io(self):
        # Mock the necessary page elements
        iframe_element = self.mocked_page.locator('iframe[id^="I0_"]').first
        iframe_element.get_attribute.return_value = 'Contacts'

        # Call the method
        self.send_email.iframe_name_io()

        # Assertions
        self.assertEqual(self.send_email._name_io, 'Contacts')

    def test_prepare_email(self):
        # Mock the necessary page elements and credentials
        self.send_email.iframe_name_io = lambda: None  # Stubbing the method for simplicity
        self.mocked_page.frame_locator.return_value.is_visible.return_value = False
        self.mocked_page.frame_locator.return_value.get_by_label.return_value.click.return_value = None

        # Define credentials
        credentials = {'name_from_contacts': 'John Doe', 'email_address_from_contacts': 'john@example.com'}

        # Call the method
        self.send_email.prepare_email(credentials)

        # Assertions for page interactions (mocked)
        self.mocked_page.frame_locator.assert_called()
        self.mocked_page.frame_locator.return_value.get_by_label.assert_called()

    def test_add_attachment(self):
        working_directory = os.getcwd()
        parent_directory = os.path.dirname(working_directory)
        path_to_file = os.path.join(parent_directory, 'files/attachment/funny_picture.png')
        file_exists = os.path.exists(path_to_file)
        self.assertTrue(file_exists, f"File {path_to_file} does not exist")

    def test_send_email(self):
        # Mock necessary page elements
        self.mocked_page.get_by_label.return_value.click.return_value = None

        # Call the method
        self.send_email.send_email()

        # Assertions for page interactions (mocked)
        self.mocked_page.get_by_label.assert_called()
