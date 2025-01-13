"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
from typing import Generator
import pytest
from playwright.sync_api import sync_playwright, Browser


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """
    Fixture to launch the browser and close it at the end of the session.

    :return: Playwright Browser object.
    """
    with sync_playwright() as p:
        start_browser = p.firefox.launch(headless=False, slow_mo=800)
        yield start_browser
        start_browser.close()
