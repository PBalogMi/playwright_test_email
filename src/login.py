from playwright.sync_api import Page


class Login:
    """
    Class for logging into an email account using provided credentials.
    """

    def __init__(self, page: Page):
        """
        Initialize the Login object with the provided Playwright Page.

        :param page: An instance of a Playwright Page object representing the current browser page.
        """
        self.page = page

    def execute_login(self, credentials: dict) -> None:
        """
        Log into the email account using provided credentials.

        :param credentials: A dictionary containing 'email' and 'password'.
                            'email': The email address to log in.
                            'password': The password for the email account.

        :return: None
        """
        self.page.get_by_label("Email or phone").fill(credentials["email"])
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_label("Enter your password").fill(credentials["password"])
        self.page.get_by_role("button", name="Next").click()
