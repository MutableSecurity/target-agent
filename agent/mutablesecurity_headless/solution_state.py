from mutablesecurity import config
from mutablesecurity.leader import Connection, ConnectionFactory
from mutablesecurity.main import Main


class SolutionState:
    tests_results: dict
    information: dict

    def __init__(self, tests_results: dict, information: dict) -> None:
        self.tests_results = tests_results
        self.information = information

    def to_dict(self) -> dict:
        return self.__dict__


class SolutionStateFactory:
    local_connection: Connection

    def __init__(self) -> None:
        config.headless = True

        self.__create_local_connection()

    def __create_local_connection(self) -> None:
        self.local_connection = ConnectionFactory().create_connection(
            user_password=None
        )

    def __execute_operation(
        self, solution_id: str, operation_name: str
    ) -> dict:
        results = Main().run(
            [self.local_connection],
            solution_id,
            operation_name,
            {"identifier": None},
        )

        return results[-1].additional_data.concrete_objects

    def get_state_of_solution(self, solution_id: str) -> SolutionState:
        tests_results = self.__execute_operation(solution_id, "test")
        information = self.__execute_operation(solution_id, "get_information")

        return SolutionState(tests_results, information)
