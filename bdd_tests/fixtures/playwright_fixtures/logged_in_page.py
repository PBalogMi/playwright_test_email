"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
from typing import Generator
import pytest

from playwright.sync_api import BrowserContext, Page


@pytest.fixture(scope="session")
def logged_in_page(context: BrowserContext) -> Generator[Page, None, None]:
    """
    Fixture that navigates to the Gmail homepage.

    :param browser: Playwright Browser object.
    :param context: Playwright BrowserContext object.
    :return: The initialized page.
    """
    page = context.new_page()
    page.goto("https://gmail.com")
    yield page
    page.close()   # Close the page at the end of the session
