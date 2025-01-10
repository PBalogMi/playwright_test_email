"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import json

class JsonWriter:
    """
    A class to handle writing data to JSON files.

    This class provides methods to update existing JSON files with new data and to completely rewrite JSON files.

    Attributes:
        path_to_file (str): The path to the JSON file.
    """

    def __init__(self, path_to_file: str):
        """
        Initializes the JsonWriter with the path to the JSON file.

        :param path_to_file: The path to the JSON file.
        """
        self.path_to_file = path_to_file

    def update_to_json_file(self, data: dict) -> None:
        """
        Stores the incoming dictionary data into the JSON file.

        :param data: The dictionary data to store in the JSON file.
        :return: None
        """

        with open(self.path_to_file, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)

        # Update existing data with new data
        existing_data.update(data)

        # Write the updated data back to the JSON file
        with open(self.path_to_file, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

    def rewrite_json_file(self, data: dict) -> None:
        """
        Remove old data completly from file and replace it with new data.
        
        :param data: The dictionary data to store in the JSON file.
        :return: None
        """
        with open(self.path_to_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
