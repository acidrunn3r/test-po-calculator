import tkinter as tk
from .presenter import CalculatorPresenter

class CalculatorGUI:
    def __init__(self, root, presenter: CalculatorPresenter):
        self.presenter = presenter
        self.root = root
        root.title("Calculator")

        self.entry_a = tk.Entry(root, name="entry_a")
        self.entry_a.grid(row=0, column=0, columnspan=2)

        self.entry_b = tk.Entry(root, name="entry_b")
        self.entry_b.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="Result", name="label_result")
        self.result_label.grid(row=2, column=0, columnspan=2)

        self.plus_button = tk.Button(root, text="+", command=self.on_plus, name="btn_plus")
        self.plus_button.grid(row=3, column=0)
        self.minus_button = tk.Button(root, text="-", command=self.on_minus, name="btn_minus")
        self.minus_button.grid(row=3, column=1)
        self.mul_button = tk.Button(root, text="*", command=self.on_multiply, name="btn_mul")
        self.mul_button.grid(row=4, column=0)
        self.div_button = tk.Button(root, text="/", command=self.on_divide, name="btn_div")
        self.div_button.grid(row=4, column=1)

    def on_plus(self):
        self.presenter.on_plus_clicked()

    def on_minus(self):
        self.presenter.on_minus_clicked()

    def on_multiply(self):
        self.presenter.on_multiply_clicked()

    def on_divide(self):
        self.presenter.on_divide_clicked()
