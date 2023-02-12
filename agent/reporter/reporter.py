import requests
from urllib3.exceptions import InsecureRequestWarning

from agent.config import ConfigurationManager
from agent.helpers.exceptions import (InvalidAPIKeyException,
                                      InvalidRequestsException)

# The package is defined dynamically and it actually exists.
# pylint: disable=no-member
requests.packages.urllib3.disable_warnings(  # type: ignore[attr-defined]
    category=InsecureRequestWarning,
)

ORCHESTRATOR_REPORT_ROUTE = "report"


class Reporter:
    config: ConfigurationManager
    api_key: str
    request_url: str

    def __init__(self) -> None:
        self.config = ConfigurationManager()
        self.api_key = self.config.api_key

        self.__build_report_url()

    def __build_report_url(self) -> None:
        self.request_url = (
            "https://"
            + self.config.orchestration_agent_address
            + ":"
            + str(self.config.orchestration_agent_port)
            + "/"
            + ORCHESTRATOR_REPORT_ROUTE
        )

    def report_data(self, data: dict) -> None:
        sent_data = {"api_key": self.api_key, "data": data}
        response = requests.post(
            self.request_url, json=sent_data, verify=False  # noqa: S501
        )

        # pylint: disable=no-member
        if response.status_code == requests.codes.unauthorized:
            raise InvalidAPIKeyException()
        elif response.status_code == requests.codes.bad_request:
            raise InvalidRequestsException()
