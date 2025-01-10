"""
This project serves as a case study on how to implement Behavior Driven Development (BDD)
testing for a Gmail account using Python, Gherkin, pytest_bdd, and Playwright.
"""
import os

class FileOperations:
    """
    A class to handle basic file operations such as ensuring the path exists,
    checking if a file exists, and deleting a file.

    Attributes:
        directory (str): The directory where the file is located.
        file_name (str): The name of the file.
        path_to_file (str): The full path to the file.
    """
    def __init__(self, directory: str, file_name: str):
        """
        Initializes the FileOperations object with the provided directory and file name.

        :param directory: The directory where the file is located.
        :param file_name: The name of the file.
        """
        self.directory = directory
        self.file_name = file_name
        self.path_to_file = os.path.join(self.directory, self.file_name)

    def _ensure_path_exists(self) -> None:
        """
        Ensures that the path to the file exists. If not, creates the path.

        :return: None
        """
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def _ensure_file_exists(self) -> bool:
        """
        Checks if the file exists.

        :return: True if the file exists, False otherwise.
        """
        return os.path.isfile(self.path_to_file)

    def delete_file(self) -> None:
        """
        Deletes the file if it exists and removes the directory if it is empty.

        :return: None
        """
        if self._ensure_file_exists():
            os.remove(self.path_to_file)
            if not os.listdir(self.directory):
                os.rmdir(self.directory)
