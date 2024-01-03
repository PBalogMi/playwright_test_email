from robot.api.deco import keyword
import os
from dotenv import dotenv_values


def get_env_vars(robot_or_bdd: str) -> str:
    """
    Retrieves environment variables from a 'config.env' file based on the given context.

    :param robot_or_bdd: Either 'robot' or another string indicating the context.

    :return: The string associated with the 'PASSWORD' key in the environment variables.
    """
    current_directory = os.getcwd()
    if robot_or_bdd == "robot":
        path_to_config = os.path.dirname(current_directory)
    else:
        path_to_config = current_directory

    path_to_file = os.path.join(path_to_config, 'config.env')
    env_vars = dotenv_values(path_to_file)
    return env_vars.get('PASSWORD', '')


@keyword
def robot_get_password_from_env() -> str:
    """
    Retrieves the password from environment variables specifically for Robot Framework Test.

    Returns:
    :return: The string associated with the 'PASSWORD' key in the environment variables.
    """
    return get_env_vars('robot')


def bdd_get_password_from_env() -> str:
    """
    Retrieves the password from environment variables for BDD scenarios.

    :return: The value associated with the 'PASSWORD' key in the environment variables.
    """
    return get_env_vars('bdd')
