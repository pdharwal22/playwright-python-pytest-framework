from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
import allure
import json
from pathlib import Path


def load_inventory_test_data():
    """
    Load product test data from products.json for pytest parameterization.
    """
    data_file_path = Path(__file__).parent.parent.parent/"test_data/products.json"
    with data_file_path.open("r", encoding="utf-8") as data_file:
        return json.load(data_file)

inventory_test_data = load_inventory_test_data()


@allure.epic("SauceDemo Application")
@allure.feature("Shopping Cart")
@allure.story("Verify Product in Cart")
@allure.title("Verify selected product is displayed in cart - {product_data[name]}")
@allure.description("Verify that each selected product appears correctly in the shopping cart.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.parametrize("product_data", inventory_test_data.values(), ids=lambda product: product["name"])
def test_product_is_displayed_in_cart(page, config, test_data, product_data):
    """
    Verify that each selected product appears in the shopping cart.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step("Retrieve valid user credentials"):
        valid_user = test_data.get("users.valid_user")[0]
        username = valid_user["username"]
        password = valid_user["password"]

    with allure.step("Login with valid credentials"):
        login_page.login(username=username, password=password)

    with allure.step("Verify inventory page is loaded"):
        inventory_page = InventoryPage(page)
        assert inventory_page.is_loaded()

    with allure.step(f"Retrieve product name: {product_data['name']}"):
        product_name = product_data["name"]

    with allure.step(f"Add {product_name} to cart"):   
        inventory_page.add_product_to_cart(product_name)

    with allure.step("Open shopping cart"):
        inventory_page.open_cart()

    with allure.step("Verify cart page is loaded"):
        cart_page = CartPage(page)
        assert cart_page.is_loaded()

    with allure.step(f"Verify '{product_name}' is present in cart"):
        assert cart_page.is_product_in_cart(product_name)

    with allure.step("Verify product name is displayed in cart"):
        product_names = cart_page.get_product_names()
        assert product_name in product_names

