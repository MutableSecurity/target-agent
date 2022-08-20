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
            "orchestration_agent_url",
            StringDataType,
            default_value=None,
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
