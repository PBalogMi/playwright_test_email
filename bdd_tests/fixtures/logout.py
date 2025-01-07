"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import pytest
from playwright.sync_api import Page

from src.logout import Logout


@pytest.fixture()
def logout(logged_in_page: Page) -> Logout:
    """
    Fixture that initializes the Logout object.

    :param logged_in_page: The initialized page.
    :return: Instance of Logout.
    """
    return Logout(logged_in_page)
