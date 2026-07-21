from config.config import ConfigManager


def test_configuration_loads_successfully():
    config = ConfigManager()

    assert config.get("application.base_url") == "https://www.saucedemo.com/"
    