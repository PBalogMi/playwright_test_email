"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
# pylint: disable=W0611
from bdd_tests.fixtures.get_env import password
from bdd_tests.fixtures.browser import browser
from bdd_tests.fixtures.context import context
from bdd_tests.fixtures.logged_in_page import logged_in_page
from bdd_tests.fixtures.login import login
from bdd_tests.fixtures.logout import logout
from bdd_tests.fixtures.send_the_email import send_the_email
