"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import pytest
from playwright.sync_api import Page

from src.login import Login


@pytest.fixture()
def login(logged_in_page: Page) -> Login:
    """
    Fixture that initializes the Login object.

    :param logged_in_page: The initialized page.
    :return: Instance of Login.
    """
    return Login(logged_in_page)
