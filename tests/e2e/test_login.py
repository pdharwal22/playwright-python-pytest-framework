from pages.login_page import LoginPage
import pytest
import allure


@allure.epic("SauceDemo Application")
@allure.feature("Authentication")
@allure.story("Valid User Login")
@allure.title("Verify valid user can login successfully")
@allure.description("Verify that a valid user can successfully log into the SauceDemo application.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
def test_valid_login(page, config, test_data):
    """
    Verify that a valid user can log in successfully.
    """

    with allure.step("Navigate to SauceDemo application"):
        login_page = LoginPage(page)
        login_page.navigate(config.get("application.base_url"))

    with allure.step("Retrieve valid user credentials"):
        username = test_data.get("users.valid_user.username")
        password = test_data.get("users.valid_user.password")

    with allure.step("Login with valid credentials"):
        login_page.login(username=username, password=password,)

    with allure.step("Verify user is successfully logged in"):
        assert page.url.endswith("/inventory.html")

