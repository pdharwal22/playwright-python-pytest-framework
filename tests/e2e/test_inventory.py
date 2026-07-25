from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
import allure


@allure.epic("SauceDemo Application")
@allure.feature("Inventory Management")
@allure.story("Add Product to Cart")
@allure.title("Verify user can add product to cart")
@allure.description("Verify that a logged-in user can add Sauce Labs Backpack to the shopping cart.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
def test_add_product_to_cart(page, config, test_data):
    """
    Verify that a user can add product to the shopping cart.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step("Retrieve valid user credentials"):
        username = test_data.get("users.valid_user.username")
        password = test_data.get("users.valid_user.password")

    with allure.step("Login with valid credentials"):
        login_page.login(username=username, password=password)

    with allure.step("Verify inventory page is loaded"):
        inventory_page = InventoryPage(page)
        assert inventory_page.is_loaded()

    with allure.step("Retrieve product name"):
        product_name = test_data.get("products.backpack.name")

    with allure.step(f"Add {product_name} to cart"):
        inventory_page.add_product_to_cart(product_name)

    with allure.step("Verify product was added to cart"):
        assert inventory_page.get_cart_item_count() == "1"

