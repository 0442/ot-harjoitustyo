from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from calculator.calculator_service import CalculatorService
from ui.base_view import _View


class LoginView(_View):
    def __init__(self,
                 root: Tk,
                 handle_back=lambda: None,
                 handle_login=lambda: None) -> None:
        self._handle_back = handle_back
        self._handle_login = handle_login
        super().__init__(root)

    def _layout(self):
        back_button = ttk.Button(master=self._frame,
                                 text="Back",
                                 command=self._handle_back)
        back_button.grid(row=0, column=0, sticky=(N, W))

        box = ttk.LabelFrame(master=self._frame,
                             text="Log in", padding="15 15 15 15")
        box.grid(row=1, column=0, sticky=(NW, SE))

        username_label = ttk.Label(master=box, text="Username")
        username_input = ttk.Entry(master=box)

        password_label = ttk.Label(master=box, text="Password")
        password_input = ttk.Entry(master=box)

        submit_button = ttk.Button(master=box,
                                   text="Log in",
                                   command=self._handle_login)

        username_label.grid(row=3, column=0, sticky=(W), pady=5)
        username_input.grid(row=3, column=1, sticky=(W, E), pady=5)

        password_label.grid(row=4, column=0, sticky=(W), pady=5)
        password_input.grid(row=4, column=1, sticky=(W, E), pady=5)

        submit_button.grid(row=5, column=0)

        box.grid_columnconfigure(1, minsize=300)
