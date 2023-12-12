from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from services.calculator_service import CalculatorService
from services.user_service import UserService
from ui.base_view import BaseView
from ui.calculator_tabs import *


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
        heading = ttk.Label(master=self._frame, text="Calculators")
        login_button = ttk.Button(master=self._frame,
                                  text="Log in",
                                  command=self._nav_login)

        logout_button = ttk.Button(master=self._frame,
                                   text="Log out",
                                   command=self._log_out)

        hist_button = ttk.Button(master=self._frame,
                                 text="History",
                                 command=self._nav_hist)
        sep = ttk.Separator(self._frame)

        tabs_cont = ttk.Notebook(master=self._frame)
        matrix_calc = MatrixCalculator(tabs_cont, self._calculator)
        echelon_calc = EchelonCalculator(tabs_cont, self._calculator)
        tabs_cont.add(child=matrix_calc.frame, text="Matrix calculator")
        tabs_cont.add(child=echelon_calc.frame, text="Row echelon calculator")

        # Clear the frame before adding components
        for widget in self._frame.winfo_children():
            widget.grid_forget()

        if self._user.user is None:
            login_button.grid(row=0, column=2, sticky=(E))
        else:
            logged_in_label = ttk.Label(master=self._frame, text=self._user.user.username)
            logged_in_label.grid(row=0, column=0)
            logout_button.grid(row=0, column=2, sticky=(E))
            login_button.grid_remove()


        hist_button.grid(row=0, column=3, sticky=(W))

        sep.grid(row=1, columnspan=5, sticky=(W, E))

        heading.grid(row=2, column=0, sticky=(W, E), pady=20)

        tabs_cont.grid(row=3, column=0, columnspan=5)

        self._frame.update_idletasks()

        # self._root.grid_columnconfigure(0, weight=1, minsize=500)
        # self._root.grid_rowconfigure(0, weight=1, minsize=500)
