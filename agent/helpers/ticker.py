import time
import typing


def execute_function_periodically(
    period_in_seconds: int, callee: typing.Callable, *args: tuple
) -> None:
    def generate_ticker() -> typing.Generator[float, None, None]:
        current_time = time.time()

        while True:
            current_time += period_in_seconds
            yield max(current_time - time.time(), 0)

    ticker = generate_ticker()
    while True:
        time.sleep(next(ticker))
        callee(*args)
