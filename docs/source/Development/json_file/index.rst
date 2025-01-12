JSON file
---------   

The code serves to create a JSON file and read/write the data to it. 

**Examples of JSON file usage:**

.. code:: python

    from src.json_file.json_file import JsonFile

    DIRECTORY_TO_SHARED_CREDENTIALS = "resources"
    JSON_FILE_NAME = "shared_credentials.json"

    # Optional initialization with dictionary to have better overview what kind of keys values are used in tests
    credentials_and_password = JsonFile(directory=DIRECTORY_TO_SHARED_CREDENTIALS,
                                         file_name=JSON_FILE_NAME,
                                         json_data={"email": "",
                                                    "password": "", 
                                                    "account_name": ""})

    #Add or update to JSON file:
    credentials_and_password.update_to_json_file(data={"email": "john_smith@gmail.com"})

    #Read from JSON file:
    credentials = credentials_and_password.read_json_file()

    #Rewrite Json file completly with new data:
    credentials_and_password.rewrite_json_file(data={"email": "john_smithed@gmail.com",
                                                     "password": "unknown",
                                                     "account_name": "John Smith"})

    






