import tkinter as tk
from .presenter import CalculatorPresenter
from .calculator import Calculator

class CalculatorViewImpl:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg="#282c34")  

        self.entry_a = tk.Entry(self.root, bg="white", fg="black", font=("Arial", 14))
        self.entry_a.pack(pady=5, padx=10)
        self.entry_b = tk.Entry(self.root, bg="white", fg="black", font=("Arial", 14))
        self.entry_b.pack(pady=5, padx=10)


        self.label_result = tk.Label(self.root, text="", bg="#282c34", fg="lime", font=("Arial", 16))
        self.label_result.pack(pady=10)

        self.calc = Calculator()
        self.presenter = CalculatorPresenter(view=self, calculator=self.calc)

        button_bg = "#61afef"
        button_fg = "black"
        button_font = ("Arial", 14)

        tk.Button(self.root, text="+", command=self.presenter.on_plus_clicked,
                  bg=button_bg, fg=button_fg, font=button_font, width=5).pack(pady=2)
        tk.Button(self.root, text="-", command=self.presenter.on_minus_clicked,
                  bg=button_bg, fg=button_fg, font=button_font, width=5).pack(pady=2)
        tk.Button(self.root, text="*", command=self.presenter.on_multiply_clicked,
                  bg=button_bg, fg=button_fg, font=button_font, width=5).pack(pady=2)
        tk.Button(self.root, text="/", command=self.presenter.on_divide_clicked,
                  bg=button_bg, fg=button_fg, font=button_font, width=5).pack(pady=2)

    def print_result(self, result):
        self.label_result["text"] = str(result)
        self.label_result["fg"] = "lime"

    def display_error(self, message):
        self.label_result["text"] = f"Error: {message}"
        self.label_result["fg"] = "red"   

    def get_first_argument_as_string(self):
        return self.entry_a.get()

    def get_second_argument_as_string(self):
        return self.entry_b.get()

    def run(self):
        self.root.mainloop()
