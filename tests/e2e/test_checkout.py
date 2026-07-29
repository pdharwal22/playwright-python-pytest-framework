from flows.checkout_flow import CheckoutFlow
import pytest
import allure
import json
from pathlib import Path


def load_checkout_test_data():
    """
    Load checkout customer data from checkout.json.
    """
    data_file_path = Path(__file__).parent.parent.parent/"test_data/checkout.json"
    with data_file_path.open("r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    return data

checkout_test_data = load_checkout_test_data()


@allure.epic("SauceDemo Application")
@allure.feature("Checkout")
@allure.story("Complete Product Checkout")
@allure.title("Verify checkout flow - {product_data[name]} - {customer_data[test_id]}")
@allure.description("Verify that a user can successfully complete the checkout flow using different products and customer information.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.parametrize("checkout_data", checkout_test_data["customers"], ids=lambda data: data["test_id"])
def test_complete_checkout_flow(authenticated_page, test_data, checkout_data):
    """
    Verify that a user can complete a complete product purchase flow using data-driven product and customer combinations.
    """

    with allure.step("Initialize checkout flow"):
        checkout_flow = CheckoutFlow(authenticated_page)


    with allure.step("Retrieve product test data"):
        product_name = test_data.get("products.backpack.name")


    with allure.step(f"Retrieve customer data for {checkout_data['test_id']}"):
        first_name = checkout_data["first_name"]
        last_name = checkout_data["last_name"]
        postal_code = checkout_data["postal_code"]


    with allure.step(f"Add {product_name} to cart"):
        checkout_flow.add_product_to_cart(product_name)


    with allure.step("Open shopping cart"):
        checkout_flow.open_cart()


    with allure.step("Verify selected product is present in cart"):
        assert checkout_flow.verify_product_in_cart(product_name)


    with allure.step("Proceed to checkout"):
        checkout_flow.proceed_to_checkout()


    with allure.step("Verify checkout information page is loaded"):
        assert checkout_flow.is_checkout_page_loaded()


    with allure.step(f"Enter customer information for {checkout_data['test_id']}"):
        checkout_flow.enter_customer_information(first_name=first_name, last_name=last_name, postal_code=postal_code)


    with allure.step("Continue to checkout overview"):
        checkout_flow.continue_to_overview()


    with allure.step("Verify checkout overview page is loaded"):
        assert checkout_flow.is_checkout_overview_loaded()


    with allure.step(f"Verify '{product_name}' is present in order overview"):
        assert checkout_flow.verify_product_in_order(product_name)


    with allure.step("Finish order"):
        checkout_flow.finish_order()


    with allure.step("Verify order completion"):
        assert checkout_flow.is_order_completed()

