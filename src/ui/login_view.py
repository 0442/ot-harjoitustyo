from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from calculator.calculator_app import App
from ui.base_view import BaseView


class LoginView(BaseView):
    def __init__(self,
                 root: Tk,
                 app: App,
                 handle_back=lambda: None) -> None:
        self._handle_back = handle_back

        self._app = app
        self._notif = StringVar()
        self._username = StringVar()
        self._password = StringVar()
        super().__init__(root)

    def _log_in(self):
        success, notif = self._app.log_in(self._username.get(),
                                          self._password.get())
        if success == False:
            self._notif.set(notif)
        else:
            self._handle_back()

    def _register(self):
        _, notif = self._app.register(self._username.get(),
                                      self._password.get())
        self._notif.set(notif)

    def _layout(self):
        back_button = ttk.Button(master=self._frame,
                                 text="Back",
                                 command=self._handle_back)
        back_button.grid(row=0, column=0, sticky=(N, W))

        box = ttk.LabelFrame(master=self._frame,
                             text="Log in", padding="15 15 15 15")
        box.grid(row=1, column=0, sticky=(NW, SE))

        notif_label = ttk.Label(master=box, textvariable=self._notif)

        username_label = ttk.Label(master=box, text="Username")
        username_input = ttk.Entry(master=box, textvariable=self._username)

        password_label = ttk.Label(master=box, text="Password")
        password_input = ttk.Entry(master=box, textvariable=self._password)

        login_button = ttk.Button(master=box,
                                  text="Log in",
                                  command=self._log_in)
        register_button = ttk.Button(master=box,
                                     text="Register",
                                     command=self._register)

        notif_label.grid(row=3, column=0, columnspan=5)
        username_label.grid(row=4, column=0, sticky=(W), pady=5)
        username_input.grid(row=4, column=1, sticky=(W, E), pady=5)

        password_label.grid(row=5, column=0, sticky=(W), pady=5)
        password_input.grid(row=5, column=1, sticky=(W, E), pady=5)

        login_button.grid(row=6, column=0)
        register_button.grid(row=6, column=1)

        box.grid_columnconfigure(1, minsize=300)
