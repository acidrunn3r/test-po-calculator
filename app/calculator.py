from __future__ import annotations

class Calculator:
    DIVIDE_THRESHOLD = 10e-8

    def sum(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if abs(b) < self.DIVIDE_THRESHOLD:
            raise ArithmeticError(f"Divider too close to zero: |{b}| < {self.DIVIDE_THRESHOLD}")
        return a / b
