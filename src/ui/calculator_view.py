from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from calculator.calculator_service import CalculatorService
from ui.base_view import _View
from ui.calculator_tabs import *


class CalculatorView(_View):
    def __init__(self,
                 root: Tk,
                 calculator: CalculatorService,
                 nav_login=lambda: None,
                 nav_hist=lambda: None) -> None:
        self._calculator = calculator
        self._nav_login = nav_login
        self._nav_hist = nav_hist
        super().__init__(root)

    def _layout(self):
        page_label = ttk.Label(master=self._frame, text="Home")
        heading = ttk.Label(master=self._frame, text="Calculators")
        login_button = ttk.Button(master=self._frame,
                                  text="Log in",
                                  command=self._nav_login)
        hist_button = ttk.Button(master=self._frame,
                                 text="History",
                                 command=self._nav_hist)
        sep = ttk.Separator(self._frame)

        tabs_cont = ttk.Notebook(master=self._frame)
        matrix_calc = MatrixCalculator(tabs_cont, self._calculator)
        echelon_calc = EchelonCalculator(tabs_cont, self._calculator)
        tabs_cont.add(child=matrix_calc.frame, text="Matrix calculator")
        tabs_cont.add(child=echelon_calc.frame, text="Row echelon calculator")

        page_label.grid(row=0, column=0, sticky=(W, N))
        login_button.grid(row=0, column=1)
        hist_button.grid(row=0, column=2)

        sep.grid(row=1, columnspan=2, sticky=(W, E))

        heading.grid(row=2, column=0, sticky=(W, E), pady=20)

        tabs_cont.grid(row=3, column=0)

        # self._root.grid_columnconfigure(0, weight=1, minsize=500)
        # self._root.grid_rowconfigure(0, weight=1, minsize=500)
