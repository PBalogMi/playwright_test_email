import os

class FileOperations:
    def __init__(self, directory: str, file_name: str):
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
