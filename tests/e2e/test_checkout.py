from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
import allure


@allure.epic("SauceDemo Application")
@allure.feature("Checkout")
@allure.story("Valid User Login")
@allure.title("Verify valid user can login successfully")
@allure.description("Verify that a valid user can successfully log into the SauceDemo application.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_complete_checkout_flow(page, config, test_data):
    """
    Verify that a user can complete a complete product purchase flow.
    """

    # --------------------------------
    # Login
    # --------------------------------
    login_page = LoginPage(page)
    login_page.navigate(config.get("application.base_url"))
    username = test_data.get("users.valid_user.username")
    password = test_data.get("users.valid_user.password")
    login_page.login(username=username, password=password)


    # --------------------------------
    # Add Product
    # --------------------------------
    inventory_page = InventoryPage(page)
    product_name = test_data.get("products.backpack.name")
    inventory_page.add_product_to_cart(product_name)


    # --------------------------------
    # Open Cart
    # --------------------------------
    inventory_page.open_cart()
    cart_page = CartPage(page)
    assert cart_page.is_loaded()
    assert cart_page.is_product_in_cart(product_name)


    # --------------------------------
    # Checkout
    # --------------------------------
    cart_page.click_checkout()
    checkout_page = CheckoutPage(page)
    assert checkout_page.is_loaded()


    # --------------------------------
    # Customer Information
    # --------------------------------
    checkout_page.enter_customer_information(first_name="Prateek", last_name="Dharwal", postal_code="141001")
    checkout_page.click_continue()


    # --------------------------------
    # Checkout Overview
    # --------------------------------
    checkout_overview_page = CheckoutOverviewPage(page)
    assert checkout_overview_page.is_loaded()
    assert checkout_overview_page.is_product_in_order(product_name)


    # --------------------------------
    # Complete Order
    # --------------------------------
    checkout_overview_page.click_finish()


    # --------------------------------
    # Verify Completion
    # --------------------------------
    checkout_complete_page = CheckoutCompletePage(page)
    assert (checkout_complete_page.get_confirmation_message() == "Thank you for your order!")

