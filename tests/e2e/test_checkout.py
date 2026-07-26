from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
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


def load_product_test_data():
    """
    Load product data from products.json.
    """
    data_file_path = Path(__file__).parent.parent.parent/"test_data/products.json"
    with data_file_path.open("r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    return data

checkout_test_data = load_checkout_test_data()
product_test_data = load_product_test_data()

# Create test combinations:
# Every product will be tested with every customer.
checkout_test_cases = [
    (product_data, customer_data)
    for product_data in product_test_data.values()
    for customer_data in checkout_test_data["valid_customers"]
]

checkout_test_ids = [
    f"{product_data['name']} - {customer_data['test_id']}"
    for product_data, customer_data in checkout_test_cases
]


@allure.epic("SauceDemo Application")
@allure.feature("Checkout")
@allure.story("Complete Product Checkout")
@allure.title("Verify checkout flow - {product_data[name]} - {customer_data[test_id]}")
@allure.description("Verify that a user can successfully complete the checkout flow using different products and customer information.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.parametrize("product_data, customer_data", checkout_test_cases, ids=checkout_test_ids)
def test_complete_checkout_flow(page, config, test_data, product_data, customer_data):
    """
    Verify that a user can complete a complete product purchase flow using data-driven product and customer combinations.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step("Retrieve valid user credentials"):
        valid_user = test_data.get("users.valid_user")[0]
        username = valid_user["username"]
        password = valid_user["password"]

    with allure.step(f"Login with user: {valid_user['test_id']}"):
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

    with allure.step(f"Verify {product_name} is present in cart"):
        assert cart_page.is_product_in_cart(product_name)

    with allure.step("Proceed to checkout"):
        cart_page.click_checkout()

    with allure.step("Verify checkout information page is loaded"):
        checkout_page = CheckoutPage(page)
        assert checkout_page.is_loaded()

    with allure.step(f"Enter customer information for {customer_data['test_id']}"):
        checkout_page.enter_customer_information(first_name=customer_data["first_name"], last_name=customer_data["last_name"], postal_code=customer_data["postal_code"])

    with allure.step("Continue to checkout overview"):
        checkout_page.click_continue()

    with allure.step("Verify checkout overview page is loaded"):
        checkout_overview_page = CheckoutOverviewPage(page)
        assert checkout_overview_page.is_loaded()

    with allure.step(f"Verify {product_name} is present in order"):
        assert checkout_overview_page.is_product_in_order(product_name)

    with allure.step("Complete the order"):
        checkout_overview_page.click_finish()

    with allure.step("Verify order confirmation message"):
        checkout_complete_page = CheckoutCompletePage(page)
        assert (checkout_complete_page.get_confirmation_message() == "Thank you for your order!")

