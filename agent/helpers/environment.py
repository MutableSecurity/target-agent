import os

from agent.helpers.exceptions import EnvironmentVariableNotFoundException


def get_environment_variable(name: str) -> str:
    if name not in os.environ:
        raise EnvironmentVariableNotFoundException()

    return os.environ[name]
