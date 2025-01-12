"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import unittest
from unittest.mock import MagicMock
from src.send_the_email import SendEmail

class TestSendEmail(unittest.TestCase):
    """
    Unit tests for the SendEmail class.
    """

    def setUp(self):
        """
        Set up the test case with a mock Page object and an instance of SendEmail.
        """
        self.mock_page = MagicMock()
        self.send_email = SendEmail(self.mock_page)

    def test_iframe_name_io(self):
        """
        Test the iframe_name_io method to ensure it correctly sets the iframe name.
        """
        # Mock the locator and get_attribute methods
        mock_iframe_element = MagicMock()
        self.mock_page.locator.return_value.first = mock_iframe_element
        mock_iframe_element.get_attribute.return_value = 'mocked_iframe_name'

        # Call the method
        self.send_email.iframe_name_io()

        # Assert the iframe name is set correctly
        # pylint: disable=protected-access
        self.assertEqual(self.send_email._name_io, 'mocked_iframe_name')

    def test_prepare_email(self):
        """
        Test the prepare_email method to ensure it correctly prepares the email.
        """
        # Mock the iframe_name_io method
        self.send_email.iframe_name_io = MagicMock()
        # pylint: disable=protected-access
        self.send_email._name_io = 'mocked_iframe_name'

        # Mock the credentials
        credentials = {
            'name_from_contacts': 'John Doe',
            'email_address_from_contacts': 'john.doe@example.com'
        }

        # Call the method
        self.send_email.prepare_email(credentials)

        # Assert the correct methods were called
        self.mock_page.frame_locator.assert_any_call('iframe[name="mocked_iframe_name"]')
        self.mock_page.frame_locator().get_by_label.assert_any_call("Search")
        self.mock_page.frame_locator().get_by_placeholder().fill.assert_called_with("John Doe")
        self.mock_page.frame_locator().get_by_label().click.assert_called()
        self.mock_page.get_by_placeholder().fill.assert_called_with("test")
        self.mock_page.get_by_role().fill.assert_called_with("test\n")

    def test_prepare_email_for_attachement(self):
        """
        Test the prepare_email_for_attachement method to ensure it correctly prepares the email with an attachment.
        """
        # Mock the iframe_name_io method
        self.send_email.iframe_name_io = MagicMock()
        # pylint: disable=protected-access
        self.send_email._name_io = 'mocked_iframe_name'

        # Call the method
        self.send_email.prepare_email_for_attachement()

        # Assert the correct methods were called
        self.mock_page.frame_locator.assert_any_call('iframe[name="mocked_iframe_name"]')
        self.mock_page.frame_locator().get_by_label().click.assert_called()
        self.mock_page.get_by_placeholder().fill.assert_called_with("test with attachement")
        self.mock_page.get_by_role().fill.assert_called_with("test with funny picture\n")
