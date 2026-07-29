import pytest
from config.config import ConfigManager
from playwright.sync_api import sync_playwright
from core.browser_manager import BrowserManager
from core.test_data_manager import TestDataManager
from pathlib import Path
from datetime import datetime
import allure
from flows.authentication_flow import AuthenticationFlow


def pytest_addoption(parser):
    """
    Add custom command-line options to pytest.
    """
    parser.addoption("--env", action="store", default=None, help="Environment to run tests against. Example: qa, staging, prod")


@pytest.fixture(scope="session")
def config(request):
    """
    Provide a single ConfigManager instance for the entire test session.
    """

    # Get environment from pytest command line
    environment = request.config.getoption("--env")

    # Create ConfigManager with explicit environment
    config_manager = ConfigManager(environment=environment)

    return config_manager


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
def context(browser, config):
    """
    Create an isolated browser context for each test.
    """
    context_instance = browser.new_context()
    if config.get("reports.trace"):
        context_instance.tracing.start(screenshots=True, snapshots=True, sources=True)
    
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


@pytest.fixture(scope="function")
def authenticated_page(page, config, test_data):
    """
    Create a new page and authenticate a valid user.
    This fixture is used by tests that require an already authenticated SauceDemo session.
    """
    
    authentication_flow = AuthenticationFlow(page=page, config=config, test_data=test_data)
    authentication_flow.login_as_valid_user()
    return page


@pytest.fixture(scope="session")
def test_data():
    """
    Provide test data to tests.
    """
    data_manager = TestDataManager()
    data_manager.load_data(file_name="users.json", data_key="users")
    data_manager.load_data(file_name="products.json", data_key="products")
    data_manager.load_data(file_name="checkout.json", data_key="checkout")
    return data_manager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture test result and attach it to the test item.
    """

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def capture_failure_artifacts(request, config):
    """
    Capture screenshot and Playwright trace when a test fails
    and attach them to the Allure report.
    """

    yield

    # Get the test execution report
    report = getattr(request.node, "rep_call", None)

    # Only continue if the test actually failed
    if not report or not report.failed:
        return

    # Try to retrieve page and context from the test request.
    # This prevents unit tests from unnecessarliy creating Playwright objects.
    page = request.node.funcargs.get("page")
    context = request.node.funcargs.get("context")

    # If the test doesn't use Playwright, there is nothing to capture.
    if page is None or context is None:
        return
    
    # Create report directories
    screenshot_directory = Path("reports/screenshots")
    trace_directory = Path("reports/traces")

    screenshot_directory.mkdir(parents=True, exist_ok=True)
    trace_directory.mkdir(parents=True, exist_ok=True)

    # Get a safe test name
    test_name = request.node.name

    # --------------------------------
    # Screenshot
    # --------------------------------
    if config.get("reports.take_screenshot_on_failure"):
        screenshot_path = screenshot_directory/f"{test_name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"\nScreenshot saved: {screenshot_path}")

        # Attach screenshot to Allure
        # with open(screenshot_path, "rb") as screenshot:
        #     allure.attach.file(screenshot.read(), name=f"{test_name} - Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(str(screenshot_path), name=f"{test_name} - Failure Screenshot", attachment_type=allure.attachment_type.PNG)

    # --------------------------------
    # Playwright Trace
    # --------------------------------
    if config.get("reports.trace"):
        trace_path = (trace_directory/f"{test_name}.zip")
        if config.get("reports.trace"):
            context.tracing.stop(path=str(trace_path))
        print(f"Trace saved: {trace_path}")

        # Attach trace to Allure
        # with open(trace_path, "rb") as trace:
        #     allure.attach.file(trace.read(), name=f"{test_name} - Playwright Trace", attachment_type=allure.attachment_type.ZIP)
        allure.attach.file(str(trace_path), name=f"{test_name} - Playwright Trace", attachment_type=allure.attachment_type.ZIP)


def pytest_configure(config):
    """
    Create a unqiue HTML report path for every test execution.
    """
    if not config.option.htmlpath:
        report_directory = Path("reports/html")
        report_directory.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        report_path = report_directory / f"report_{timestamp}.html"
        config.option.htmlpath = str(report_path)

