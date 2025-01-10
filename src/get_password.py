"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import os
from robot.api.deco import keyword
from dotenv import dotenv_values

@keyword
def get_password_from_env() -> str:
    """
    Retrieves the 'PASSWORD' environment variable from the 'config.env' file.

    :return: The string associated with the 'PASSWORD' key in the environment variables.
    """
    current_directory = os.getcwd()
    path_to_file = os.path.join(current_directory, 'config.env')
    env_vars = dotenv_values(path_to_file)
    return env_vars.get('PASSWORD', '')
