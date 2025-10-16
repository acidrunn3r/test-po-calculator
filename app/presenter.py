from __future__ import annotations
from typing import Optional
from .calculator import Calculator
from .view import CalculatorView

class CalculatorPresenter:
    def __init__(self, view: CalculatorView, calculator: Optional[Calculator] = None):
        self.view = view
        self.calculator = calculator or Calculator()

    def _parse_args(self):
        a_str = self.view.get_first_argument_as_string()
        b_str = self.view.get_second_argument_as_string()

        if a_str is None or a_str.strip() == "":
            raise ValueError("First argument is empty")
        if b_str is None or b_str.strip() == "":
            raise ValueError("Second argument is empty")

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError as e:
            raise ValueError("Arguments must be numbers") from e
        return a, b

    def on_plus_clicked(self):
        try:
            a, b = self._parse_args()
            result = self.calculator.sum(a, b)
            self.view.print_result(result)
        except Exception as e:
            self.view.display_error(str(e))

    def on_minus_clicked(self):
        try:
            a, b = self._parse_args()
            result = self.calculator.subtract(a, b)
            self.view.print_result(result)
        except Exception as e:
            self.view.display_error(str(e))

    def on_multiply_clicked(self):
        try:
            a, b = self._parse_args()
            result = self.calculator.multiply(a, b)
            self.view.print_result(result)
        except Exception as e:
            self.view.display_error(str(e))

    def on_divide_clicked(self):
        try:
            a, b = self._parse_args()
            result = self.calculator.divide(a, b)
            self.view.print_result(result)
        except Exception as e:
            self.view.display_error(str(e))
