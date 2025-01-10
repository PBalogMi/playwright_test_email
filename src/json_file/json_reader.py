import json


class JsonReader:
    def __init__(self, path_to_file: str):
        """
        Initializes the JsonReader with the path to the JSON file.

        :param path_to_file: The path to the JSON file.
        """
        self.path_to_file = path_to_file

    def read_json_file(self) -> dict:
        """
        Reads the JSON file and returns the data as a dictionary.

        :return: Data from the JSON file as a dictionary.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """

        with open(self.path_to_file, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON from file {self.path_to_file}: {e}") from e
