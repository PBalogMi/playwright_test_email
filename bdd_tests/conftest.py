"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
# pylint: disable=W0611
from bdd_tests.fixtures.playwright_fixtures.browser import browser
from bdd_tests.fixtures.playwright_fixtures.context import context
from bdd_tests.fixtures.playwright_fixtures.logged_in_page import logged_in_page

from bdd_tests.fixtures.bdd_tests_fixtures.get_env import password
from bdd_tests.fixtures.bdd_tests_fixtures.login import login
from bdd_tests.fixtures.bdd_tests_fixtures.logout import logout
from bdd_tests.fixtures.bdd_tests_fixtures.send_the_email import send_the_email
