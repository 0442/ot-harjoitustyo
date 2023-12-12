from tkinter import Tk, ttk, StringVar, IntVar, Text
from tkinter.constants import *

from services.calculator_service import CalculatorService, str_to_matrix
from ui.base_view import BaseView


class MatrixCalculator(BaseView):
    def __init__(self, root: Tk, calculator: CalculatorService) -> None:
        super().__init__(root)
        self._calculator = calculator

    def _layout(self):
        input_label = ttk.Label(master=self._frame, text="Expression")
        expr_input = ttk.Entry(master=self._frame)

        empty = ttk.Separator(master=self._frame)
        empty.grid(row=0, column=0)

        input_label.grid(row=0, column=0)
        expr_input.grid(row=0, column=1)

        self._root.grid_columnconfigure(1, minsize=300)


class EchelonCalculator(BaseView):
    def __init__(self, root: Tk, calculator: CalculatorService) -> None:
        self._calculator = calculator
        self._input_var = StringVar()
        self._output_var = StringVar()
        self._interp_var = StringVar()
        super().__init__(root)

    def _layout(self):
        guide_label = ttk.Label(master=self._frame,
                                text=("Input a matrix consisting of "
                                      "integers or rational numbers."))
        example_label = ttk.Label(master=self._frame,
                                  text="e.g. [[1/2, 3, 2], [2/3, 1, 3]]")
        input_label = ttk.Label(master=self._frame, text="Matrix")
        input_field = ttk.Entry(master=self._frame,
                                textvar=self._input_var)

        interp_label = ttk.Label(master=self._frame, textvar=self._interp_var)

        output_label = ttk.Label(master=self._frame, text="Result")
        output_field = ttk.Entry(master=self._frame,
                                 textvar=self._output_var)

        submit_button = ttk.Button(master=self._frame,
                                   text="Row reduce",
                                   command=self._handle_submit)

        guide_label.grid(row=0, column=0, columnspan=2)
        example_label.grid(row=1, column=1)
        input_label.grid(row=2, column=0)
        input_field.grid(row=2, column=1, sticky=(W,E))
        interp_label.grid(row=3, column=1)
        output_label.grid(row=4, column=0)
        output_field.grid(row=4, column=1, sticky=(W,E))
        submit_button.grid(row=5, column=1, sticky=(W,E), pady=15)

        self._root.grid_columnconfigure(1, minsize=300)

    def _handle_submit(self):
        try:
            expr = self._input_var.get()
            self._interp_var.set(f"Interpreted as: {str_to_matrix(expr)}")
            result = self._calculator.row_reduce(expr)
            self._output_var.set(result)
        except Exception as e:
            print(e)
            self._interp_var.set(f"Invalid input")
            self._output_var.set("")
