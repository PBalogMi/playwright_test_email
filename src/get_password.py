"""
The get_password.py file contains the function get_password_from_env that reads the password from the 
config.env file and serves also for the Robot framework.
"""
import os
from robot.api.deco import keyword
from dotenv import dotenv_values

@keyword
def get_password_from_env() -> str:
    """
    Retrieves the 'PASSWORD' environment variable from the 'config.env' file.

    :return: The string associated with the 'PASSWORD' key in the environment variables.
    """
    current_directory = os.getcwd()
    path_to_file = os.path.join(current_directory, 'config.env')
    env_vars = dotenv_values(path_to_file)
    return env_vars.get('PASSWORD', '')
