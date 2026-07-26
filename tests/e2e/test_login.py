from pages.login_page import LoginPage
import pytest
import allure
import json
from pathlib import Path


def load_login_test_data():
    """
    Load login test data directly from users.json for pytest parameterization.
    """
    data_file_path = (Path(__file__).parent.parent.parent/"test_data"/"users.json")

    with data_file_path.open("r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    return data

login_test_data = load_login_test_data()


@allure.epic("SauceDemo Application")
@allure.feature("Authentication")
@allure.story("Valid User Login")
@allure.title("Verify valid user can login successfully")
@allure.description("Verify that a valid user can successfully log into the SauceDemo application.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize("user_data", login_test_data["valid_user"], ids=lambda user: user["test_id"])
def test_valid_login(page, config, user_data):
    """
    Verify that a valid user can log in successfully.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    # with allure.step("Retrieve valid user credentials"):
    #     username = test_data.get("users.valid_user.username")
    #     password = test_data.get("users.valid_user.password")
    
    with allure.step(f"Retrieve credentials for {user_data['test_id']}"):
        username = user_data["username"]
        password = user_data["password"]

    # with allure.step("Login with valid credentials"):
    #     login_page.login(username=username, password=password,)

    with allure.step(f"Login with user: {user_data['test_id']}"):
        login_page.login(username=username, password=password)

    with allure.step("Verify user is successfully logged in"):
        # assert page.url.endswith("/inventory.html")
        assert page.url.endswith(user_data["expected_url"])


@allure.epic("SauceDemo Application")
@allure.feature("Authentication")
@allure.story("Invalid User Login")
@allure.title("Verify invalid user login is rejected")
@allure.description("Verify that invalid or locked-out users cannot log into the SauceDemo application.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.parametrize("user_data", login_test_data["invalid_users"], ids=lambda user: user["test_id"])
def test_invalid_login(page, config, user_data):
    """
    Verify that invalid users cannot log in successfully.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step(f"Login with user: {user_data['test_id']}"):
        login_page.login(username=user_data["username"], password=user_data["password"])

    with allure.step("Verify login error message"):
        error_message = page.locator('[data-test="error"]')
        assert error_message.is_visible()
        assert error_message.inner_text() == user_data["expected_error"]

