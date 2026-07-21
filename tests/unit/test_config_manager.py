import pytest
from config.config import ConfigManager


def test_configuration_loads_successfully():
    config = ConfigManager()

    assert config.get("application.base_url") == "https://www.saucedemo.com/"


def test_browser_configuration():
    config = ConfigManager()

    assert config.get("browser.name") == "chromium"
    assert config.get("browser.headless") is False
    assert config.get("browser.slow_mo") == 0


def test_timeout_configuration():
    config = ConfigManager()

    assert config.get("timeouts.default") == 30000
    assert config.get("timeouts.navigation") == 60000


def test_report_configuration():
    config = ConfigManager()

    assert config.get("reports.take_screenshot_on_failure") is True
    assert config.get("reports.record_video") is False
    assert config.get("reports.trace") is True


def test_empty_configuration_key_raises_error():
    config = ConfigManager()

    with pytest.raises(ValueError):
        config.get("")


def test_invalid_configuration_key_raises_error():
    config = ConfigManager()

    with pytest.raises(KeyError):
        config.get("invalid.key")

