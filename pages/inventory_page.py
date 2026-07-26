from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import get_logger


class InventoryPage(BasePage):
    """
    Page Object representing the SauceDemo inventory page.
    """

    logger = get_logger(__name__)

    INVENTORY_CONTAINER = "[data-test='inventory-container']"
    SHOPPING_CART = "[data-test='shopping-cart-link']"

    def __init__(self, page: Page):
        super().__init__(page)


    def is_loaded(self) -> bool:
        """
        Check whether the inventory page is displayed.
        """
        # return self.is_visible(self.INVENTORY_CONTAINER)
        is_loaded = self.is_visible(self.INVENTORY_CONTAINER)
        self.logger.info("Inventory page loaded: %s", is_loaded)
        return is_loaded
    

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Add a product to the shopping cart using its product name.
        """
        # product = self.page.locator(".inventory_item").filter(has_text=product_name)
        # product.locator("button").click()
        
        self.logger.info("Adding product to cart: %s", product_name)
        product_slug = product_name.lower().replace(" ", "-")
        add_to_cart_button = (f"[data-test='add-to-cart-{product_slug}']")
        self.click(add_to_cart_button)
        self.logger.info("Product added to cart: %s", product_name)

        # self.logger.info("Adding product to cart: %s", product_name)
        # product = (self.page.locator(".inventory_item").filter(has_text=product_name))
        # product.locator(".button").click()
        # self.logger.info("Product added to cart: %s", product_name)

    
    def open_cart(self) -> None:
        """
        Open the shopping cart.
        """
        self.click(self.SHOPPING_CART)

    
    def get_cart_item_count(self) -> str:
        """
        Return the number displayed on the shopping cart badge.
        """
        return self.page.locator(".shopping_cart_badge").inner_text()
    
