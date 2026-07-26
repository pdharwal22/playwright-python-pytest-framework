from pages.inventory_page import InventoryPage
# from pages.login_page import LoginPage
import pytest
import allure
import json
from pathlib import Path


def load_inventory_test_data():
    """
    Load inventory test data directly from products.json for pytest parameterization.
    """
    data_file_path = Path(__file__).parent.parent.parent/"test_data/products.json"
    with data_file_path.open("r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    return data

inventory_test_data = load_inventory_test_data()


@allure.epic("SauceDemo Application")
@allure.feature("Inventory Management")
@allure.story("Add Product to Cart")
@allure.title("Verify user can add product to cart - {product_data[name]}")
@allure.description("Verify that a logged-in user can add different products to the shopping cart.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize("product_data", inventory_test_data.values(), ids=lambda product: product["name"])
def test_add_product_to_cart(authenticated_page, product_data):
    """
    Verify that a user can add different products to the shopping cart.
    """

    # with allure.step("Navigate to SauceDemo application"):
    #     login_page = LoginPage(page)
    #     login_page.navigate(config.get("application.base_url"))

    # with allure.step("Retrieve valid user credentials"):
    #     valid_user = test_data.get("users.valid_user")[0]
    #     username = valid_user["username"]
    #     password = valid_user["password"]

    # with allure.step("Login with valid credentials"):
    #     login_page.login(username=username, password=password)

    with allure.step("Verify inventory page is loaded"):
        inventory_page = InventoryPage(authenticated_page)
        assert inventory_page.is_loaded()

    with allure.step(f"Retrieve product name: {product_data['name']}"):
        product_name = product_data['name']

    with allure.step(f"Add {product_name} to cart"):
        inventory_page.add_product_to_cart(product_name)

    with allure.step(f"Verify {product_name} was added to cart"):
        assert inventory_page.get_cart_item_count() == "1"

