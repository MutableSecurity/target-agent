from agent.helpers.ticker import execute_function_periodically
from agent.mutablesecurity_headless import LocalSystem
from agent.reporter import Reporter


class Agent:
    reporter: Reporter
    state: LocalSystem

    def __init__(self) -> None:
        self.state = LocalSystem()
        self.reporter = Reporter()

    def get_and_report_local_state(self) -> None:
        state = self.state.get_all_solutions_state()
        self.reporter.report_data(state)

    def start(self) -> None:
        execute_function_periodically(
            1,
            self.get_and_report_local_state,
        )


def main() -> None:
    Agent().start()


if __name__ == "__main__":
    main()
