from flows.shopping_cart_flow import ShoppingCartFlow
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

class CheckoutFlow:
    """
    Business workflow responsible for completing a SauceDemo checkout.
    """

    def __init__(self, page):
        self.page = page

        self.shopping_cart_flow = ShoppingCartFlow(page)
        self.checkout_page = CheckoutPage(page)
        self.checkout_overview_page = CheckoutOverviewPage(page)
        self.checkout_complete_page = CheckoutCompletePage(page)


    def add_product_to_cart(self, product_name: str) -> None:
        """
        Add a specified product to the shopping cart.
        """
        self.shopping_cart_flow.add_product_to_cart(product_name)


    def open_cart(self) -> None:
        """
        Open the shopping cart.
        """
        self.shopping_cart_flow.open_cart()


    def verify_product_in_cart(self, product_name: str) -> None:
        """
        Verify that the specified product exists in the shopping cart.
        """
        return self.shopping_cart_flow.verify_product_in_cart(product_name)


    def proceed_to_checkout(self) -> None:
        """
        Procees from the shopping cart to the checkout page.
        """
        self.shopping_cart_flow.proceed_to_checkout()


    def is_checkout_page_loaded(self) -> bool:
        """
        Verify that the checkout information page is loaded.
        """
        return self.checkout_page.is_loaded()


    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Enter customer information required for checkout.
        """
        self.checkout_page.enter_customer_information(first_name=first_name, last_name=last_name, postal_code=postal_code)


    def continue_to_overview(self) -> None:
        """
        Continue from customer information to checkout overview.
        """
        self.checkout_page.click_continue()


    def is_checkout_overview_loaded(self) -> bool:
        """
        Verify that the checkout overview page is loaded.
        """
        return self.checkout_overview_page.is_loaded()


    def verify_product_in_order(self, product_name: str) -> bool:
        """
        Verify that the specified product is present in the order overview.
        """
        return self.checkout_overview_page.is_product_in_order(product_name)


    def finish_order(self) -> None:
        """
        Complete the order.
        """
        self.checkout_overview_page.click_finish()


    def is_order_completed(self) -> bool:
        """
        Verify that the order completion page is displayed.
        """
        return self.checkout_complete_page.get_confirmation_message() == "Thank you for your order!"