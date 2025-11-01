import pytest
import tkinter as tk
from app.gui import CalculatorGUI
from app.presenter import CalculatorPresenter
from app.view import TkinterCalculatorView

@pytest.fixture
def gui_app():
    root = tk.Tk()
    root.withdraw()
    view = None
    presenter = None
    gui = CalculatorGUI(root, presenter)
    view = TkinterCalculatorView(gui)
    presenter = CalculatorPresenter(view=view)
    gui.presenter = presenter
    yield gui
    root.destroy()

def test_plus_button(gui_app):
    gui_app.entry_a.insert(0, "2")
    gui_app.entry_b.insert(0, "3")
    gui_app.plus_button.invoke()
    assert gui_app.result_label["text"] == "5.0"

def test_minus_button(gui_app):
    gui_app.entry_a.insert(0, "10")
    gui_app.entry_b.insert(0, "4")
    gui_app.minus_button.invoke()
    assert gui_app.result_label["text"] == "6.0"

def test_multiply_button(gui_app):
    gui_app.entry_a.insert(0, "3")
    gui_app.entry_b.insert(0, "5")
    gui_app.mul_button.invoke()
    assert gui_app.result_label["text"] == "15.0"

def test_divide_button(gui_app):
    gui_app.entry_a.insert(0, "8")
    gui_app.entry_b.insert(0, "2")
    gui_app.div_button.invoke()
    assert gui_app.result_label["text"] == "4.0"
