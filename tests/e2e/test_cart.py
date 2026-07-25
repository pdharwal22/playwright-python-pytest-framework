from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
import allure


@allure.epic("SauceDemo Application")
@allure.feature("Shopping Cart")
@allure.story("Verify Product in Cart")
@allure.title("Verify selected product is displayed in cart")
@allure.description("Verify that a selected product appears correctly in the shopping cart.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.e2e
def test_product_is_displayed_in_cart(page, config, test_data):
    """
    Verify that a selected product appears in the shopping cart.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step("Retrieve valid user credentials"):
        username = test_data.get("users.valid_user.username")
        password = test_data.get("users.valid_user.password")

    with allure.step("Login with valid credentials"):
        login_page.login(username=username, password=password)

    with allure.step("Retrieve product name"):
        product_name = test_data.get("products.backpack.name")

    with allure.step(f"Add {product_name} to cart"):   
        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart(product_name)

    with allure.step("Open shopping cart"):
        inventory_page.open_cart()

    with allure.step("Verify cart page is loaded"):
        cart_page = CartPage(page)
        assert cart_page.is_loaded()

    with allure.step(f"Verify '{product_name}' is present in cart"):
        assert cart_page.is_product_in_cart(product_name)

