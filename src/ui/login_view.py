from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from services.user_service import UserService
from ui.base_view import BaseView
from entities.user import User


class LoginView(BaseView):
    def __init__(self,
                 root: Tk,
                 users: UserService,
                 handle_back=lambda: None) -> None:
        self._handle_back = handle_back

        self._users = users
        self._notif = StringVar()
        self._username = StringVar()
        self._password = StringVar()
        super().__init__(root)

    def _log_in(self):
        user = User(self._username.get(), self._password.get())
        success, notif = self._users.log_in(user)
        if success == False:
            self._notif.set(notif)
        else:
            self._handle_back()

    def _register(self):
        user = User(self._username.get(), self._password.get())
        _, notif = self._users.register(user)
        self._notif.set(notif)

    def _layout(self):
        back_button = ttk.Button(master=self._frame,
                                 text="Back",
                                 command=self._handle_back)
        back_button.grid(row=0, column=0, sticky=(N, W))

        box = ttk.LabelFrame(master=self._frame,
                             text="Log in", padding="15 15 15 15")
        box.grid(row=1, column=0, sticky=(N, S, E, W))

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

        self._frame.grid_rowconfigure(0, weight=0)
        box.grid_columnconfigure(0, weight=0)
        box.grid_columnconfigure(1, weight=1)

        notif_label.grid(row=0, column=0, columnspan=5)
        username_label.grid(row=1, column=0, sticky=(W), pady=5)
        username_input.grid(row=1, column=1, sticky=(W, E), pady=5)

        password_label.grid(row=2, column=0, sticky=(W), pady=5)
        password_input.grid(row=2, column=1, sticky=(W, E), pady=5)

        login_button.grid(row=3, column=0, sticky=(W))
        register_button.grid(row=3, column=1, sticky=(W))
