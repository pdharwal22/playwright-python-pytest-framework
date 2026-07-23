from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.regression
@pytest.mark.e2e
def test_product_is_displayed_in_cart(page, config):
    """
    Verify that a selected product appears in the shopping cart.
    """
    login_page = LoginPage(page)
    login_page.navigate(config.get("application.base_url"))
    login_page.login(username="standard_user", password="secret_sauce")
    
    inventory_page = InventoryPage(page)
    product_name = "Sauce Labs Backpack"
    inventory_page.add_product_to_cart(product_name)
    inventory_page.open_cart()
    
    cart_page = CartPage(page)
    assert cart_page.is_loaded()
    assert cart_page.is_product_in_cart(product_name)

