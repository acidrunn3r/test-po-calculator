from typing import Protocol

class CalculatorView(Protocol):
    def print_result(self, result: float) -> None:
        ...

    def display_error(self, message: str) -> None:
        ...

    def get_first_argument_as_string(self) -> str:
        ...

    def get_second_argument_as_string(self) -> str:
        ...
