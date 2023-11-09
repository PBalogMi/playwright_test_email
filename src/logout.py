class Logout:

    def __init__(self, page):
        self.page = page

    def execute_logout(self, credentials):
        account_name = credentials["account_name"]
        email = credentials["email"]
        self.page.get_by_label(f"Účet Google: {account_name}  \n({email})").click()
        self.page.frame_locator("iframe[name=\"account\"]").get_by_role("link", name="Odhlásiť sa").click()
