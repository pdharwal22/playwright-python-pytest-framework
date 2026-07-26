from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):
    """
    Page Object representing the SauceDemo login page.
    """

    logger = get_logger(__name__)

    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

    
    # def enter_username(self, username: str) -> None:
    #     """
    #     Enter username into the username field.
    #     """
    #     self.fill(self.USERNAME_INPUT, username)

    
    # def enter_password(self, password: str) -> None:
    #     """
    #     Enter password into the password field.
    #     """
    #     self.fill(self.PASSWORD_INPUT, password)


    # def click_login(self) -> None:
    #     """
    #     Click the login button.
    #     """
    #     self.click(self.LOGIN_BUTTON)

    
    # def login(self, username: str, password: str) -> None:
    #     """
    #     Perform login using the provided credentials.
    #     """
    #     self.enter_username(username)
    #     self.enter_password(password)
    #     self.click_login()

    
    # def is_error_message_visible(self) -> bool:
    #     """
    #     Check whether the login error message is visible.
    #     """
    #     return self.is_visible(self.ERROR_MESSAGE)

    def login(self, username: str, password: str) -> None:
        """
        Login using the provided credentials.
        """

        self.logger.info("Attempting login with username: %s", username)
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Login action completed for username %s", username)
    
