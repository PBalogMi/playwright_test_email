class MissingDataError(Exception):
    def __init__(self, message="Shared credentials are missing in JSON file. "
                               "Rerun successfully test level 1, or correct JSON file manually."):
        self.message = message
        super().__init__(self.message)
