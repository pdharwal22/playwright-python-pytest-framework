from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object representing the SauceDemo checkout information page.
    """

    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTCAL_CODE = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"

    def __init__(self, page: Page):
        super().__init__(page)


    def is_loaded(self) -> bool:
        """
        Verify that the checkout information page is displayed.
        """
        return self.page.url.endswith("/checkout-step-one.html")
    

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str,) -> None:
        """
        Enter customer information required for checkout.
        """
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTCAL_CODE, postal_code)

    
    def click_continue(self) -> None:
        """
        Continue to checkout overview.
        """
        self.click(self.CONTINUE_BUTTON)

