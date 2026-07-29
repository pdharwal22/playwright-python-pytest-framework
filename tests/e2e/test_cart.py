from flows.shopping_cart_flow import ShoppingCartFlow
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
def test_product_is_displayed_in_cart(authenticated_page, product_data):
    """
    Verify that each selected product appears in the shopping cart.
    """

    with allure.step("Initialize shopping flow"):
        shopping_flow = ShoppingCartFlow(authenticated_page)

    with allure.step("Verify inventory page is loaded"):
        assert shopping_flow.is_inventory_loaded()

    product_name = product_data["name"]

    with allure.step(f"Add {product_name} to cart"):   
        shopping_flow.add_product_to_cart(product_name)

    with allure.step("Open shopping cart"):
        shopping_flow.open_cart()

    with allure.step("Verify cart page is loaded"):
        assert shopping_flow.is_cart_loaded()

    with allure.step(f"Verify '{product_name}' is present in cart"):
        assert shopping_flow.verify_product_in_cart(product_name)

    with allure.step("Verify product name is displayed in cart"):
        product_names = shopping_flow.get_cart_product_names()
        assert product_name in product_names

