from tkinter import Tk, ttk, scrolledtext
from tkinter.constants import *

from services.user_service import UserService
from ui.base_view import BaseView

class HistoryView(BaseView):
    def __init__(self,
                 root: Tk,
                 users: UserService,
                 handle_back=lambda: None) -> None:
        self._handle_back = handle_back

        self._users = users
        self._history = self._users.get_history()
        if self._users.user is None:
            self._history = (
                "You must log in first to view you calculation history."
            )
        elif len(self._history) == 0:
            self._history = "Empty history"

        super().__init__(root)

    def _layout(self):
        back_button = ttk.Button(master=self._frame,
                                 text="Back",
                                 command=self._handle_back)
        back_button.grid(row=0, column=0, sticky=(N, W))

        box = ttk.LabelFrame(master=self._frame,
                             text="History", padding="15 15 15 15")
        box.grid(row=1, column=0, sticky=(NW, SE))

        history_text = scrolledtext.ScrolledText(master=box)
        history_text.insert(END, self._history)
        history_text.config(state=DISABLED)

        history_text.grid(row=2, column=0, sticky=(E,W))

        box.grid_columnconfigure(0, minsize=300)
