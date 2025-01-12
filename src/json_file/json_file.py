"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import json
import os

from src.json_file.file_operations import FileOperations
from src.json_file.json_reader import JsonReader
from src.json_file.json_writer import JsonWriter

class JsonFile(FileOperations, JsonReader, JsonWriter):
    """
    A class to handle JSON file operations including reading, writing, and updating JSON files.

    This class inherits from FileOperations, JsonReader, and JsonWriter to provide a comprehensive
    set of file operations for JSON files.

    Attributes:
        directory (str): The directory where the JSON file is located.
        file_name (str): The name of the JSON file.
        json_data (dict): The data to be written to the JSON file.
        path_to_file (str): The full path to the JSON file.
    """
    def __init__(self, directory: str, file_name:str, json_data: dict = None):
        """
        Initializes the JsonFile object with the provided directory, file name, and optional JSON data.

        :param directory: The directory where the JSON file is located.
        :param file_name: The name of the JSON file.
        :param json_data: The data to be written to the JSON file. Defaults is an empty dictionary.
        """
        super().__init__(directory, file_name)
        self.json_data = json_data if json_data is not None else {}
        self.path_to_file = os.path.join(self.directory, self.file_name)
        JsonReader.__init__(self, self.path_to_file)
        JsonWriter.__init__(self, self.path_to_file)
        self.__create_json_file()

    def __create_json_file(self) -> None:
        """
        Creates a JSON file with the provided data.

        :return: None
        """
        self._ensure_path_exists()
        if self._ensure_file_exists():
            if self.json_data:
                self.__update_json_file()
        else:
            with open(self.path_to_file, 'w', encoding='utf-8') as json_file:
                json.dump(self.json_data, json_file, ensure_ascii=False, indent=4)

    def __update_json_file(self) -> None:
        """
        Updates the existing JSON file by adding new keys from json_data and removing keys not in json_data.

        :return: None
        """
        with open(self.path_to_file, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)

        # Add new keys from json_data
        for key, value in self.json_data.items():
            existing_data[key] = value

        # Remove keys not in json_data
        keys_to_remove = [key for key in existing_data if key not in self.json_data]
        for key in keys_to_remove:
            del existing_data[key]

        # Write the updated data back to the JSON file
        with open(self.path_to_file, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
