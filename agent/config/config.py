from agent.mutablesecurity.config.config import (
    ConfigurationKey,
    ConfigurationManager as GenericConfigurationManager,
)
from agent.mutablesecurity.helpers.data_type import IntegerDataType, StringDataType

from enum import Enum

class ConfigurationManager(GenericConfigurationManager):
    class ConfigurationKeys(Enum):
        """Enumeration for all the keys from the configuration file."""

        CONFIGURATION_FILENAME = ConfigurationKey(
            "configuration_filename",
            StringDataType,
            default_value=".mutablesecurity",
        )
        API_KEY = ConfigurationKey(
            "api_key",
            StringDataType,
            default_value=None,
        )
        ORCHESTRATION_AGENT_ADDRESS = ConfigurationKey(
            "orchestration_agent_address",
            StringDataType,
            default_value=None,
        )
        ORCHESTRATION_AGENT_PORT = ConfigurationKey(
            "orchestration_agent_port",
            IntegerDataType,
            default_value=40400,
        )
        REPORT_PERIOD = ConfigurationKey(
            "report_period",
            IntegerDataType,
            default_value=60,
        )

    def __init__(self) -> None:
        super().__init__(
            ".mutablesecurity",
            ConfigurationManager, 
        )