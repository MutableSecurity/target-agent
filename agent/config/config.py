from mutablesecurity.config import (
    ConfigurationKey,
    GenericConfigurationManager,
)
from mutablesecurity.helpers.data_type import IntegerDataType, StringDataType


class ConfigurationManager(GenericConfigurationManager):
    KEYS = [
        ConfigurationKey(
            "api_key",
            StringDataType,
            default_value=None,
        ),
        ConfigurationKey(
            "orchestration_agent_address",
            StringDataType,
            default_value=None,
        ),
        ConfigurationKey(
            "orchestration_agent_port",
            IntegerDataType,
            default_value=40400,
        ),
        ConfigurationKey(
            "report_period",
            IntegerDataType,
            default_value=60,
        ),
    ]
    FILENAME = ".mutablesecurity"

    def __init__(self) -> None:
        super().__init__(
            ConfigurationManager.KEYS, ConfigurationManager.FILENAME
        )
