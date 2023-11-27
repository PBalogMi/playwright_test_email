import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from src.login import Login
from src.logout import Logout
from src.send_email import SendEmail


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
    yield page
    page.close()   # Close the page at the end of the session


@pytest.fixture()
def login(logged_in_page: Page) -> Login:
    """
    Fixture that initializes the Login object.

    :param logged_in_page: The initialized page.
    :return: Instance of Login.
    """
    return Login(logged_in_page)


@pytest.fixture()
def logout(logged_in_page: Page) -> Logout:
    """
    Fixture that initializes the Logout object.

    :param logged_in_page: The initialized page.
    :return: Instance of Logout.
    """
    return Logout(logged_in_page)


@pytest.fixture()
def send_the_email(logged_in_page: Page) -> SendEmail:
    """
    Fixture that initializes the SendEmail object.

    :param logged_in_page: The initialized page.
    :return: Instance of SendEmail.
    """
    return SendEmail(logged_in_page)
