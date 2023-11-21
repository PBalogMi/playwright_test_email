import os
import json


def check_json_keys():
    required_keys = ["email", "password", "account_name"]
    working_directory = os.getcwd()
    path_to_file = os.path.join(working_directory, 'files/json_shared_credentials/json_shared_credentials.json')

    # Read the JSON file
    with open(path_to_file, 'r') as file:
        data = json.load(file)

    # Check if all required keys are present in the JSON data
    for key in required_keys:
        if key not in data:
            return True

    return False
