"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) 
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import unittest
from unittest.mock import Mock, patch
from playwright.sync_api import Page
from src.login import Login


class TestLogin(unittest.TestCase):
    """
    Unit tests for the Login class.
    """

    def setUp(self):
        """
        Set up the test case with a mock Page object and an instance of Login.
        """
        self.mocked_page = Mock(spec=Page)
        self.login = Login(self.mocked_page)

    def test_execute_login(self):
        """
        Test the execute_login method to ensure it correctly fills in the email and password fields.

        :param credentials: A dictionary containing 'email' and 'password'.
        """
        credentials = {"email": "test@example.com", "password": "test_password"}

        with patch.object(self.mocked_page, "get_by_label") as mock_get_by_label, \
                patch.object(self.mocked_page, "get_by_role") as mock_get_by_role:

            mock_get_by_label.return_value = mock_get_by_label
            mock_get_by_role.return_value = mock_get_by_role

            self.login.execute_login(credentials)

            # Ensure fill was called twice - once for email and once for password
            mock_get_by_label.fill.assert_any_call(credentials["email"])
            mock_get_by_label.fill.assert_any_call(credentials["password"])
            self.assertEqual(mock_get_by_label.fill.call_count, 2)
            mock_get_by_label.assert_any_call("Email or phone")
            mock_get_by_label.assert_any_call("Enter your password")
