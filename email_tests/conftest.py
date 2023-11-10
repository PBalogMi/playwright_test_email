import pytest
from playwright.sync_api import Page


@pytest.fixture()
def main_page(page: Page):
    """
    Fixture that navigates to the Gmail homepage.

    :param page: An instance of a Playwright Page object.
    :return:  The initialized page.
    """
    page.goto("https://gmail.com")
    yield page
