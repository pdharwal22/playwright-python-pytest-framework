from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object representing the SauceDemo shopping cart.
    """

    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "[data-test='checkout']"

    def __init__(self, page: Page):
        super().__init__(page)

    
    def is_loaded(self) -> bool:
        """
        Verify that the shopping cart page is displayed.
        """
        return self.page.url.endswith("/cart.html")
    

    def get_product_names(self) -> list[str]:
        """
        Return the names of all products currently present in the cart.
        """
        products = self.page.locator(".inventory_item_name").all_inner_texts()
        return products
    

    def is_product_in_cart(self, product_name: str) -> bool:
        """
        Verify whether a specific product exists in the shopping cart.
        """
        # return product_name in self.get_product_names()
        cart_item = self.page.locator(self.CART_ITEMS).filter(has_text=product_name)
        return cart_item.count() > 0
    

    def click_checkout(self) -> None:
        """
        Proceed to checkout.
        """
        self.click(self.CHECKOUT_BUTTON)

