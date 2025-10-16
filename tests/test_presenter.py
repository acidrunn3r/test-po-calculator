from unittest.mock import Mock
import pytest
from app.presenter import CalculatorPresenter
from app.calculator import Calculator

def make_view_mock(first="1", second="2"):
    view = Mock()
    view.get_first_argument_as_string.return_value = first
    view.get_second_argument_as_string.return_value = second
    view.print_result = Mock()
    view.display_error = Mock()
    return view

def test_on_plus_clicked_calls_print_result():
    view = make_view_mock("1.5", "2.5")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_plus_clicked()
    view.print_result.assert_called_once_with(4.0)
    view.display_error.assert_not_called()

def test_on_minus_clicked_success():
    view = make_view_mock("10", "3")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_minus_clicked()
    view.print_result.assert_called_once_with(7.0)

def test_on_multiply_clicked_success():
    view = make_view_mock("2", "4")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_multiply_clicked()
    view.print_result.assert_called_once_with(8.0)

def test_on_divide_clicked_handles_divide_by_zero_and_calls_display_error():
    view = make_view_mock("1", "0")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_divide_clicked()
    view.display_error.assert_called_once()
    view.print_result.assert_not_called()

def test_on_plus_clicked_with_invalid_input_shows_error():
    view = make_view_mock("not-a-number", "2")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_plus_clicked()
    view.display_error.assert_called_once()
    view.print_result.assert_not_called()

def test_empty_first_argument_shows_error():
    view = make_view_mock("", "2")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_plus_clicked()
    view.display_error.assert_called_once()

def test_empty_second_argument_shows_error():
    view = make_view_mock("1", "")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_plus_clicked()
    view.display_error.assert_called_once()

def test_on_plus_clicked_with_negative_numbers():
    view = make_view_mock("-5", "-3")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_plus_clicked()
    view.print_result.assert_called_once_with(-8)

def test_on_minus_clicked_with_negative_result():
    view = make_view_mock("3", "5")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_minus_clicked()
    view.print_result.assert_called_once_with(-2)

def test_on_divide_clicked_with_negative_numbers():
    view = make_view_mock("-6", "3")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_divide_clicked()
    view.print_result.assert_called_once_with(-2)

def test_on_multiply_clicked_with_negative_numbers():
    view = make_view_mock("-2", "4")
    presenter = CalculatorPresenter(view=view, calculator=Calculator())
    presenter.on_multiply_clicked()
    view.print_result.assert_called_once_with(-8)

def test_on_minus_clicked_with_invalid_input_shows_error():
    view = make_view_mock("abc", "2")
    presenter = CalculatorPresenter(view=view)
    presenter.on_minus_clicked()
    view.display_error.assert_called_once()
    view.print_result.assert_not_called()

def test_on_multiply_clicked_with_empty_input_shows_error():
    view = make_view_mock("", "5")
    presenter = CalculatorPresenter(view=view)
    presenter.on_multiply_clicked()
    view.display_error.assert_called_once()
    view.print_result.assert_not_called()