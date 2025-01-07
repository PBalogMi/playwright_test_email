"""
This project serves as a case study on how to implement Behavior Driven Development (BDD) testing for a Gmail account 
using Python, Gherkin, pytest_bdd, and Playwright.
"""
import pytest
from playwright.sync_api import Browser, BrowserContext


@pytest.fixture(scope="session")
def context(browser: Browser) -> BrowserContext:
    """
    Fixture to create a browser context.

    :param browser: Playwright Browser object.
    :return: Playwright BrowserContext object.
    """
    return browser.new_context()
