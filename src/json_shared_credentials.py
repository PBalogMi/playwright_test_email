import os
import json
from json.decoder import JSONDecodeError


def get_file_path() -> str:
    """
    Get the file path for the shared credentials JSON file.

    This function retrieves the file path for the JSON file containing shared credentials.

    :return: Path to the shared credentials JSON file.
    """
    working_directory = os.getcwd()
    path_to_file = os.path.join(working_directory, 'files/json_shared_credentials/json_shared_credentials.json')

    return path_to_file


def read_shared_credentials() -> dict:
    """
    Reads shared credentials from a JSON file or creates a new file if it doesn't exist.

    :return: Dictionary containing shared credentials.
    """
    file_path = get_file_path()
    #print(f'+++FILE SIZE++++++++++{os.stat(file_path).st_size}++++++++++++++++++++++++++')
    try:
        if os.stat(file_path).st_size == 0:
            with open(file_path, 'w') as file:
                #file.write('{}')
                json.dump({}, file)

        with open(file_path, 'r') as file:
            try:
                shared_credentials = json.load(file)
            except JSONDecodeError as e:
                print(f"JSON file was found damaged. System will rewrite old file 'json_shared_credentials.json' with "
                      f"new file and continue in testing. JSON decoding error: {e}")
                shared_credentials = {}
    except FileNotFoundError:
        # Create a new file if it doesn't exist
        shared_credentials = {}
        with open(file_path, 'w') as file:
            json.dump(shared_credentials, file)

    return shared_credentials


def update_shared_credentials(credentials: dict) -> None:
    """
    Updates or creates shared credentials in a JSON file.

    :param credentials: Dictionary containing credentials to update/add.
    """
    file_path = get_file_path()
    shared_credentials = read_shared_credentials()

    # Update the shared credentials with new data or add new keys
    shared_credentials.update(credentials)

    # Write the updated credentials back to the file
    with open(file_path, 'w') as file:
        json.dump(shared_credentials, file, indent=4)
