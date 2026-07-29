from pages.login_page import LoginPage

class AuthenticationFlow:
    """
    Business workflow responsible for authentication-related operations.
    """

    def __init__(self, page, config, test_data):
        self.page = page
        self.config = config
        self.test_data = test_data
        self.login_page = LoginPage(page)


    def login_as_valid_user(self):
        """
        Login using the first valid user from the test data.
        """
        self.login_page.navigate(self.config.get("application.base_url"))
        valid_user = self.test_data.get("users.valid_user")[0]
        self.login_page.login(username=valid_user["username"], password=valid_user["password"])

