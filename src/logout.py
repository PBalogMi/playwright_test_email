from playwright.sync_api import Page


class Logout:
    """
    Class for logging out of a Google account.
    """

    def __init__(self, page: Page):
        """
        Initialize the Logout object with the provided Playwright Page.

        :param page: An instance of a Playwright Page object representing the current browser page.
        """
        self.page = page

    def execute_logout(self, credentials: dict) -> None:
        """
        Execute the logout process for the provided Google account.

        :param credentials: A dictionary containing 'account_name' and 'email'.
                            'account_name': The name associated with the Google account.
                            'email': The email address of the Google account.
        """
        account_name = credentials["account_name"]
        email = credentials["email"]
        self.page.get_by_label(f"Google Account: {account_name}  \n({email})").click()
        self.page.frame_locator("iframe[name=\"account\"]").get_by_role("link", name="Sign out").click()
