class MissingDataError(Exception):
    """
    Exception raised when shared credentials are missing in a JSON file.
    """
    def __init__(self, message="Shared credentials are missing in JSON file. "
                               "Rerun successfully test level 1, or correct JSON file manually."):
        """
        Initializes the MissingDataError.

        Args:
            message (str, optional): Explanation of the error. Defaults to a generic message.
        """
        self.message = message
        super().__init__(self.message)
