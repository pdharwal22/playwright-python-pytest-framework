import json
from pathlib import Path
from typing import Any


class TestDataManager:
    """
    Responsible for loading and providing test data.
    """

    def __init__(self):
        self._data = {}

    
    def load_data(self, file_name: str, data_key: str) -> None:
        """
        Load test data from a JSON file and store it under the specified data key.
        """
        data_file_path = (Path(__file__).parent.parent/"test_data"/file_name)

        if not data_file_path.exists():
            raise FileNotFoundError(f"Test data file {data_file_path} not found.")
        
        with data_file_path.open("r", encoding="utf-8") as data_file:
            loaded_data = json.load(data_file)

        self._data[data_key] = loaded_data


    def get(self, key: str) -> Any:
        """
        Retrieve test data using a dot-separated key.
        """
        if not key:
            raise ValueError("Test data key cannot be empty.")
        
        value = self._data

        for part in key.split("."):
            if not isinstance(value, dict) or part not in value:
                raise KeyError(f"Test data key not found: {key}")
            
            value = value[part]
        
        return value
        

    def get_list(self, key: str) -> list:
        """
        Retrieve a list of test data using a dot-separated key.
        """
        value = self.get(key)
        if not isinstance(value, list):
            raise TypeError(f"Test data at '{key}' must be a list.")
        return value

