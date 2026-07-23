from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
@pytest.mark.e2e
def test_valid_login(page, config, test_data):
    """
    Verify that a valid user can log in successfully.
    """
    login_page = LoginPage(page)
    login_page.navigate(config.get("application.base_url"))
    username = test_data.get("users.valid_user.username")
    password = test_data.get("users.valid_user.password")
    login_page.login(username=username, password=password,)
    assert page.url.endswith("/inventory.html")

