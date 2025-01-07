"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import pytest
from playwright.sync_api import Page

from src.send_email import SendEmail


@pytest.fixture()
def send_the_email(logged_in_page: Page) -> SendEmail:
    """
    Fixture that initializes the SendEmail object.

    :param logged_in_page: The initialized page.
    :return: Instance of SendEmail.
    """
    return SendEmail(logged_in_page)
