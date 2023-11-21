import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


@pytest.fixture(scope="session")
def browser() -> Browser:
    """
    Fixture to launch the browser and close it at the end of the session.

    :return: Playwright Browser object.
    """
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=800)
        yield browser
        browser.close()  # Close the browser at the end of the session


@pytest.fixture(scope="session")
def context(browser: Browser) -> BrowserContext:
    """
    Fixture to create a browser context.

    :param browser: Playwright Browser object.
    :return: Playwright BrowserContext object.
    """
    return browser.new_context()


@pytest.fixture(scope="session")
def logged_in_page(browser: Browser, context: BrowserContext) -> Page:
    """
    Fixture that navigates to the Gmail homepage.

    :param browser: Playwright Browser object.
    :param context: Playwright BrowserContext object.
    :return: The initialized page.
    """
    page = context.new_page()
    page.goto("https://gmail.com")

    return page


@pytest.fixture()
def main_page(logged_in_page: Page) -> Page:
    """
    Fixture that provides the initialized page.

    :param logged_in_page: The logged_in_page fixture.
    :return: The initialized page.
    """
    return logged_in_page
