from tkinter import Tk, ttk, StringVar, IntVar, Text
from tkinter.constants import *

from services.calculator_service import CalculatorService
from services.user_service import UserService
from ui.base_view import BaseView
from ui.calculator_tabs import *

guide_text = (
    "Matrices can consist of integers or "
    "rational numbers. For example "
    "'[[1/2, 3, -2]]'. "
    "\n\n"
    "Supported operations in matrix "
    "calculator are '+', '-' and '*'. "
    "Calculations are done from left to right. "
    "Braces are not supported."
)


class CalculatorView(BaseView):
    def __init__(self,
                 root: Tk,
                 calculator: CalculatorService,
                 user: UserService,
                 nav_login=lambda: None,
                 nav_hist=lambda: None) -> None:
        self._calculator = calculator
        self._user = user
        self._nav_login = nav_login
        self._nav_hist = nav_hist
        super().__init__(root)

    def _log_out(self):
        self._user.log_out()
        self._layout()

    def _layout(self):
        login_button = ttk.Button(master=self._frame,
                                  text="Log in",
                                  command=self._nav_login)

        logout_button = ttk.Button(master=self._frame,
                                   text="Log out",
                                   command=self._log_out)

        hist_button = ttk.Button(master=self._frame,
                                 text="History",
                                 command=self._nav_hist)

        box = ttk.LabelFrame(master=self._frame,
                             text="Calculators", padding="15 15 15 15")

        guide = Text(master=box, wrap=WORD, height=10, width=999)
        guide.insert(END, guide_text)
        guide.config(state=DISABLED)

        tabs_cont = ttk.Notebook(master=box)
        matrix_calc = MatrixCalculator(tabs_cont, self._calculator, self._user)
        echelon_calc = EchelonCalculator(
            tabs_cont, self._calculator, self._user)
        tabs_cont.add(child=matrix_calc.frame, text="Matrix calculator")
        tabs_cont.add(child=echelon_calc.frame, text="Row echelon calculator")

        # Clear the frame before adding components
        for widget in self._frame.winfo_children():
            widget.grid_forget()

        if self._user.user is None:
            login_button.grid(row=0, column=1, sticky=(N, W))
        else:
            logged_in_label = ttk.Label(
                master=self._frame, text=self._user.user.username)

            logged_in_label.grid(row=0, column=2, sticky=(N, W))
            logout_button.grid(row=0, column=1, sticky=(N, W))
            login_button.grid_remove()

        hist_button.grid(row=0, column=0, sticky=(N, W))

        self._frame.grid_rowconfigure(0, weight=0)
        self._frame.grid_rowconfigure(1, weight=1)
        box.grid_columnconfigure(0, weight=1)
        box.grid_columnconfigure(1, weight=1)
        box.grid_rowconfigure(2, weight=1)

        box.grid(row=1, column=0, columnspan=2, sticky=(N, S, E, W))

        guide.grid(row=1, column=0, columnspan=3, sticky=(W), pady=10)

        tabs_cont.grid(row=2, column=0, columnspan=2, sticky=(N, S, E, W))

        self._frame.update_idletasks()
