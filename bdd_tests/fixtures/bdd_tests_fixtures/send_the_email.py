"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import pytest
from playwright.sync_api import Page

from src.send_the_email import SendTheEmail


@pytest.fixture()
def send_the_email(logged_in_page: Page) -> SendTheEmail:
    """
    Fixture that initializes the SendEmail object.

    :param logged_in_page: The initialized page.
    :return: Instance of SendTheEmail.
    """
    return SendTheEmail(logged_in_page)
