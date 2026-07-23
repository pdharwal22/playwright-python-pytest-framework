from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
@pytest.mark.e2e
def test_add_product_to_cart(page, config, test_data):
    """
    Verify that a user can add product to the shopping cart.
    """
    login_page = LoginPage(page)
    login_page.navigate(config.get("application.base_url"))
    username = test_data.get("users.valid_user.username")
    password = test_data.get("users.valid_user.password")
    login_page.login(username=username, password=password)

    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()

    product_name = test_data.get("products.backpack.name")
    inventory_page.add_product_to_cart(product_name)
    assert inventory_page.get_cart_item_count() == "1"

