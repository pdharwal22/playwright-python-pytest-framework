import pytest
from config.config import ConfigManager


@pytest.fixture
def config():
    """
    Proivde a ConfigManager instance for tests.
    """
    return ConfigManager()

