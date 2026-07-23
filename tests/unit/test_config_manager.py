import pytest


@pytest.mark.unit
def test_configuration_loads_successfully(config):
    assert config.get("application.base_url") == "https://www.saucedemo.com/"


@pytest.mark.unit
def test_browser_configuration(config):
    assert config.get("browser.name") == "chromium"
    assert config.get("browser.headless") is False
    assert config.get("browser.slow_mo") == 700


def test_timeout_configuration(config):
    assert config.get("timeouts.default") == 30000
    assert config.get("timeouts.navigation") == 60000


def test_report_configuration(config):
    assert config.get("reports.take_screenshot_on_failure") is True
    assert config.get("reports.record_video") is False
    assert config.get("reports.trace") is True


def test_empty_configuration_key_raises_error(config):
    with pytest.raises(ValueError):
        config.get("")


def test_invalid_configuration_key_raises_error(config):
    with pytest.raises(KeyError):
        config.get("invalid.key")

