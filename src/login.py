class Login:

    def __init__(self, page):
        self.page = page

    def execute_login(self, credentials):
        self.page.get_by_label("Email or phone").fill(credentials["email"])
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_label("Enter your password").fill(credentials["password"])
        self.page.get_by_role("button", name="Next").click()
