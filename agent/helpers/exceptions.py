from agent.mutablesecurity.helpers.exceptions import MutableSecurityException


class ReporterException(MutableSecurityException):
    """An error occurred while reporting to the orchestration server."""


class InvalidAPIKeyException(ReporterException):
    """The set API key is invalid."""


class InvalidRequestsException(ReporterException):
    """The requests sent to the orchestration server are invalid."""


class EnvironmentException(MutableSecurityException):
    """An error occurred while interacting with the environment."""


class EnvironmentVariableNotFoundException(EnvironmentException):
    """The environment key was not found."""
