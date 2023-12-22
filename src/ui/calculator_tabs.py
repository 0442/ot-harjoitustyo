from tkinter import Tk, ttk, StringVar, IntVar, Text, scrolledtext
from tkinter.constants import *

from services.calculator_service import CalculatorService, str_to_matrix
from services.user_service import UserService
from ui.base_view import BaseView


class MatrixCalculator(BaseView):
    def __init__(self, root: Tk, calculator: CalculatorService, user: UserService) -> None:
        self._calculator = calculator
        self._user = user
        self._input_var = StringVar()
        self._interp_var = StringVar()
        self._output_var = StringVar()

        super().__init__(root)

    def _handle_submit(self):
        try:
            expr = self._input_var.get()
            result = self._calculator.matrix_calc(expr)
            self._output_var.set(result)
            self._interp_var.set("")

            self._user.append_history(expr, result)
        except ValueError as e:
            self._interp_var.set(e)

    def _layout(self):
        input_label = ttk.Label(master=self._frame, text="Expression")

        input_field = ttk.Entry(master=self._frame,
                                textvar=self._input_var)

        guide_label = ttk.Label(master=self._frame,
                                text=("Input a matrix consisting of "
                                      "integers or rational numbers."))
        example_label = ttk.Label(master=self._frame,
                                  text="e.g. [[1/2, 3, 2], [2/3, 1, 3]] + [[1,2,3], [4,5,6]]")

        interp_label = ttk.Label(master=self._frame, textvar=self._interp_var)

        output_label = ttk.Label(master=self._frame, text="Result")
        output_field = ttk.Entry(master=self._frame,
                                 textvar=self._output_var)

        submit_button = ttk.Button(master=self._frame,
                                   text="Calculate",
                                   command=self._handle_submit)

        self._frame.grid_columnconfigure(0, weight=0)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_rowconfigure(0, weight=0)

        guide_label.grid(row=0, column=0, columnspan=2)
        example_label.grid(row=1, column=0, columnspan=2)
        input_label.grid(row=3, column=0, padx=10)
        input_field.grid(row=3, column=1, sticky=(W, E))
        interp_label.grid(row=4, column=1)
        output_label.grid(row=5, column=0, padx=10)
        output_field.grid(row=5, column=1, sticky=(W, E))
        submit_button.grid(row=6, column=1, sticky=(W, E), pady=15)

        self._root.grid_columnconfigure(1, minsize=300)


class EchelonCalculator(BaseView):
    def __init__(self, root: Tk, calculator: CalculatorService, user: UserService) -> None:
        self._calculator = calculator
        self._user = user
        self._input_var = StringVar()
        self._output_var = StringVar()
        self._interp_var = StringVar()

        self._steps_textbox = None

        super().__init__(root)

    def _handle_submit(self):
        try:
            expr = self._input_var.get()
            expr_as_matrix = str_to_matrix(expr)

            self._interp_var.set(f"Interpreted as: {expr_as_matrix}")
            answer, solution = self._calculator.row_reduce(expr)
            self._output_var.set(answer)

            self._steps_textbox.delete("1.0", END)
            self._steps_textbox.insert(END, solution)

            self._user.append_history(str(expr_as_matrix), str(answer))
        except Exception as e:
            print(e)
            self._interp_var.set(f"Invalid input")
            self._output_var.set("")

    def _layout(self):
        self._steps_textbox = scrolledtext.ScrolledText(master=self._frame)

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

        self._frame.grid_columnconfigure(0, weight=0)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_rowconfigure(0, weight=0)
        self._frame.grid_rowconfigure(5, weight=1)

        guide_label.grid(row=0, column=0, columnspan=2)
        example_label.grid(row=1, column=1, columnspan=2)
        input_label.grid(row=2, column=0, padx=10)
        input_field.grid(row=2, column=1, sticky=(W, E))
        interp_label.grid(row=3, column=1)
        output_label.grid(row=4, column=0, padx=10)
        output_field.grid(row=4, column=1, sticky=(W, E))
        self._steps_textbox.grid(row=5, column=1, sticky=(W, E, N, S))
        submit_button.grid(row=6, column=1, sticky=(W, E), pady=15)

        self._root.grid_columnconfigure(1, minsize=300)
