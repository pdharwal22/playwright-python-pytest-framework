import pytest

@pytest.mark.smoke
def test_browser_launch(page, config):
    """
    Verify that the configured browser can launch and navigate to the application.
    """
    print(f"Running tests against environment: {config.get_environment}")
    page.goto(config.get("application.base_url"))
    assert page.title() == "Swag Labs"

