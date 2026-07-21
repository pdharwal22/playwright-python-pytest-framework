"""
Configuration management for the automation framework.
"""

from typing import Any
from dotenv import load_dotenv
import os
from pathlib import Path
import json


class ConfigManager:
    """
    Responsible for loading and providing framework configuration.
    """

    def __init__(self):
        self._environment = None
        self._config = {}

        # self initialization configuration manager
        self.load_environment()
        self.load_configuration()
        self.validate()

    def load_environment(self) -> None:
        """
        Load the active environment from the .env file.
        """
        load_dotenv()
        self._environment = os.getenv("ENVIRONMENT")
        if not self._environment:
            raise ValueError("ENVIRONMENT variable not set in .env file.")


    def load_configuration(self) -> None:
        """
        Load configuration from the active environment JSON file.
        """
        if not self._environment:
            raise RuntimeError("Environment is not loaded. Call load_environment() first.")
        
        config_file_path = Path(__file__).parent / "environments" / f"{self._environment}.json"
        
        if not config_file_path.exists():
            raise FileNotFoundError(f"Configuration file {config_file_path} not found.")
        
        with config_file_path.open("r", encoding="utf-8") as config_file:
            self._config = json.load(config_file)

    def validate(self) -> None:
        """
        Validate the loaded configuration to ensure all required keys are present.
        """
        if not self._config:
            raise RuntimeError("Configuration is not loaded. Call load_configuration() first.")
        required_keys = {
            "application": ["base_url"],
            "browser": ["name", "headless", "slow_mo"],
            "timeouts": ["default", "navigation"],
            "reports": [
                "take_screenshot_on_failure",
                "record_video",
                "trace"
            ]
        }

        for category, keys in required_keys.items():
            if category not in self._config:
                raise ValueError(f"Missing requiredconfiguration category: {category}")
            for key in keys:
                if key not in self._config[category]:
                    raise KeyError(f"Missing configuration key: {category}.{key}")
                

    def get(self, key: str) -> Any:
        """
        Retrieve a configuration value by key using a dot notation.

        Example:
            config.get("application.base_url")
            config.get("browser.headless")
            config.get("timeouts.default")
        """
        if not key:
            raise ValueError("Configuration key cannot be empty.")
        
        keys = key.split(".")
        value = self._config

        for current_key in keys:
            if not isinstance(value, dict) or current_key not in value:
                raise KeyError(f"Configuration key not found: {key}")
            
            value = value[current_key]
        
        return value

if __name__ == "__main__":
    config = ConfigManager()
    print("Configuration loaded and validated successfully.")

    print("Environment: ", config._environment)
    print("Base URL: ", config.get("application.base_url"))
    print("Browser: ", config.get("browser.name"))
    print("Headless: ", config.get("browser.headless"))
    print("Default Timeout: ", config.get("timeouts.default"))
    print("Trace: ", config.get("reports.trace"))
