import pytest
from playwright.sync_api import Page


@pytest.fixture()
def main_page(page: Page):
    page.goto("https://gmail.com")
    yield page