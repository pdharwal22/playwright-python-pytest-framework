import pytest
from config.config import ConfigManager
from playwright.sync_api import sync_playwright
from core.browser_manager import BrowserManager
from core.test_data_manager import TestDataManager


@pytest.fixture(scope="session")
def config():
    """
    Provide a single ConfigManager instance for the entire test session.
    """
    return ConfigManager()


@pytest.fixture(scope="session")
def playwright():
    """
    Start the Playwright engine for the test session.
    """
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser_manager(playwright, config):
    """
    Provide a BrowserManager instance.
    """
    return BrowserManager(playwright=playwright, config=config,)


@pytest.fixture(scope="session")
def browser(browser_manager):
    """
    Launch the configured browser.
    """
    browser_instance = browser_manager.launch_browser()
    
    yield browser_instance

    browser_manager.close()


@pytest.fixture(scope="function")
def context(browser):
    """
    Create an isolated browser context for each test.
    """
    context_instance = browser.new_context()
    
    yield context_instance

    context_instance.close()


@pytest.fixture(scope="function")
def page(context):
    """
    Create a new browser for each test.
    """
    page_instance = context.new_page()

    yield page_instance

    page_instance.close()


@pytest.fixture(scope="session")
def test_data():
    """
    Provide test data to tests.
    """
    data_manager = TestDataManager()
    data_manager.load_data(file_name="users.json", data_key="users")
    data_manager.load_data(file_name="products.json", data_key="products")
    return data_manager

