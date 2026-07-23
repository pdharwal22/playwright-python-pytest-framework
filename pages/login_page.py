from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object representing the SauceDemo login page.
    """

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    
    def enter_username(self, username: str) -> None:
        """
        Enter username into the username field.
        """
        self.fill(self.USERNAME_INPUT, username)

    
    def enter_password(self, password: str) -> None:
        """
        Enter password into the password field.
        """
        self.fill(self.PASSWORD_INPUT, password)


    def click_login(self) -> None:
        """
        Click the login button.
        """
        self.click(self.LOGIN_BUTTON)

    
    def login(self, username: str, password: str) -> None:
        """
        Perform login using the provided credentials.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    
    def is_error_message_visible(self) -> bool:
        """
        Check whether the login error message is visible.
        """
        return self.is_visible(self.ERROR_MESSAGE)
    
