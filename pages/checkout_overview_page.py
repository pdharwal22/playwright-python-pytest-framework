from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """
    Page Object representing the SauceDemo checkout overview page.
    """

    CART_ITEMS = ".cart-item"
    FINISH_BUTTON = "[data-test='finish']"

    def __init__(self, page: Page):
        super().__init__(page)

    
    def is_loaded(self) -> bool:
        """
        Verify that the checkout overview page is displayed.
        """
        return self.page.url.endswith("/checkout-step-two.html")
    

    def is_product_in_order(self, product_name: str) -> None:
        """
        Verify that a specific product appears in the order summary.
        """
        products = self.page.locator(".inventory_item_name").all_inner_texts()
        return product_name in products
    

    def click_finish(self) -> None:
        """
        Complete the order.
        """
        self.click(self.FINISH_BUTTON)

