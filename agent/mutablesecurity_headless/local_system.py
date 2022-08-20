import os
import typing

from agent.mutablesecurity_headless.solution_state import SolutionStateFactory

MUTABLESECURITY_HOME = "/opt/mutablesecurity"


class LocalSystem:
    def get_all_solutions_state(self) -> dict:
        factory = SolutionStateFactory()

        states = {}
        for solution_id in self.__get_local_solutions():
            solution_state = factory.get_state_of_solution(solution_id)
            states[solution_id] = solution_state.to_dict()

        return states

    def __get_local_solutions(self) -> typing.Generator[str, None, None]:
        for solution_id in os.listdir(MUTABLESECURITY_HOME):
            yield solution_id
