from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """
    Page Object representing the completed SauceDemo checkout page.
    """

    COMPLETE_HEADER = "[data-test='complete-header']"

    def __init__(self, page: Page):
        super().__init__(page)

    
    def is_loaded(self) -> bool:
        """
        Verify that the checkout complete page is displayed.
        """
        return self.page.url.endswith("/checkout-complete.html")
    

    def get_confirmation_message(self) -> str:
        """
        Return the order confirmation message.
        """
        return self.page.locator(self.COMPLETE_HEADER).inner_text()
    
