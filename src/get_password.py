from robot.api.deco import keyword
import os
from dotenv import dotenv_values


@keyword
def get_password_from_env() -> str:
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    path_to_file = os.path.join(parent_directory, 'config.env')
    env_vars = dotenv_values(path_to_file)
    return env_vars.get('PASSWORD', '')
