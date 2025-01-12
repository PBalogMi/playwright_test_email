"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) 
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import os
import unittest
from unittest.mock import patch

from src.get_password import get_password_from_env

class TestGetPasswordFromEnv(unittest.TestCase):
    """
    Unit tests for the get_password_from_env function.
    """

    @patch('src.get_password.dotenv_values')
    @patch('os.getcwd')
    def test_get_password_from_env(self, mock_getcwd, mock_dotenv_values):
        """
        Test the get_password_from_env function to ensure it correctly retrieves the password
        from the config.env file.

        :param mock_getcwd: Mock for os.getcwd function.
        :param mock_dotenv_values: Mock for dotenv_values function.
        """        
        # Mock the current working directory
        mock_getcwd.return_value = '/mocked/path'

        # Mock the dotenv_values function to return a specific value
        mock_dotenv_values.return_value = {'PASSWORD': 'mocked_password'}

        # Call the function
        password = get_password_from_env()

        # Assert the password is as expected
        self.assertEqual(password, 'mocked_password')

        # Construct the expected path using os.path.join
        expected_path = os.path.join('/mocked/path', 'config.env')

        # Assert the path to the config file is correct
        mock_dotenv_values.assert_called_once_with(expected_path)
