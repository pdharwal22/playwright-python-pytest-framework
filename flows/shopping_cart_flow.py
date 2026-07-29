from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class ShoppingCartFlow:
    """
    Business workflow responsible for shopping-related operations.
    """

    def __init__(self, page):
        self.page = page
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)


    def is_inventory_loaded(self) -> bool:
        """
        Verify that the inventory page is loaded.
        """
        return self.inventory_page.is_loaded()


    def is_cart_loaded(self) -> bool:
        """
        Verify that the shopping cart page is loaded.
        """
        return self.cart_page.is_loaded()


    def add_product_to_cart(self, product_name: str) -> None:
        """
        Add a specified product to the shopping cart.
        """
        if not self.inventory_page.is_loaded():
            raise RuntimeError("Inventory page is not loaded. Cannot add product to cart.")
        self.inventory_page.add_product_to_cart(product_name)


    def open_cart(self) -> None:
        """
        Open the shopping cart.
        """
        if not self.inventory_page.is_loaded():
            raise RuntimeError("Inventory page is not loaded. Cannot open shopping cart.")
        self.inventory_page.open_cart()


    def verify_product_in_cart(self, product_name: str) -> bool:
        """
        Verify that a specified product exists in the shopping cart.
        """
        if not self.cart_page.is_loaded():
            raise RuntimeError("Shopping cart page is not loaded. Cannot verify cart contents.")
        return self.cart_page.is_product_in_cart(product_name)


    def get_cart_product_names(self) -> list[str]:
        """
        Return the names of all products currently in the cart.
        """
        if not self.cart_page.is_loaded():
            raise RuntimeError("Shopping cart page is not loaded. Cannot retrieve cart products.")
        return self.cart_page.get_product_names()


    def proceed_to_checkout(self) -> None:
        """
        Proceed from the shopping cart to checkout.
        """
        if not self.cart_page.is_loaded():
            raise RuntimeError("Shopping cart page is not loaded. Cannot proceed to checkout.")
        self.cart_page.click_checkout()

