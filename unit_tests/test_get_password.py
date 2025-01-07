"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import unittest
from unittest.mock import patch
from src.get_password_for_robot import get_env_vars, robot_get_password_from_env, bdd_get_password_from_env


class TestEnvVars(unittest.TestCase):
    def test_get_env_vars(self):
        # Mocking os.getcwd and dotenv_values for unit test
        with patch('os.getcwd', return_value='/path/to/config'):
            with patch('src.get_password.dotenv_values') as mock_dotenv_values:
                mock_dotenv_values.return_value = {'PASSWORD': 'test_password'}

                # Test when robot_or_bdd is 'robot'
                result_robot = get_env_vars('robot')
                mock_dotenv_values.assert_called_once_with('/path/to/config.env')
                self.assertEqual(result_robot, 'test_password')

                # Test when robot_or_bdd is 'bdd'
                result_bdd = get_env_vars('bdd')
                mock_dotenv_values.assert_called_with('/path/to/config/config.env')
                self.assertEqual(result_bdd, 'test_password')

    def test_robot_get_password_from_env(self):
        # Mocking get_env_vars for unit test
        with patch('src.get_password.get_env_vars', return_value='mocked_password'):
            result = robot_get_password_from_env()
            self.assertEqual(result, 'mocked_password')

    def test_bdd_get_password_from_env(self):
        # Mocking get_env_vars for unit test
        with patch('src.get_password.get_env_vars', return_value='mocked_password'):
            result = bdd_get_password_from_env()
            self.assertEqual(result, 'mocked_password')
