"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import os
from typing import Generator
import pytest
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../config.env'))

@pytest.fixture(scope="session")
def password() -> Generator[str, None, None]:
    """
    Fixture to provide the password from the config.env file.

    :yield: Password string.
    :rtype: Generator[str, None, None]
    """
    password_from_env = os.getenv("PASSWORD")
    if not password_from_env or password_from_env == "****":
        raise ValueError("PASSWORD not found in config.env")
    yield password_from_env
