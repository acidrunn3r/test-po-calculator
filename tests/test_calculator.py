import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_sum(calc):
    assert calc.sum(3.5, 2.0) == 5.5

def test_subtract(calc):
    assert calc.subtract(5.0, 2.0) == 3.0

def test_multiply(calc):
    assert calc.multiply(3.0, 4.0) == 12.0

def test_divide_normal(calc):
    assert pytest.approx(calc.divide(5.0, 2.0), rel=1e-9) == 2.5

def test_divide_small_denominator_raises(calc):
    with pytest.raises(ArithmeticError):
        calc.divide(1.0, 1e-9)

def test_sum_negative(calc):
    assert calc.sum(-1, -2) == -3

def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2

def test_multiply_by_zero(calc):
    assert calc.multiply(5, 0) == 0

def test_multiply_negative(calc):
    assert calc.multiply(-3, 3) == -9

def test_divide_negative(calc):
    assert calc.divide(-6, 3) == -2

def test_divide_positive_small(calc):
    assert pytest.approx(calc.divide(1e-5, 1), rel=1e-9) == 1e-5

def test_divide_exact_threshold(calc):
    result = calc.divide(1, calc.DIVIDE_THRESHOLD)
    assert result > 0
