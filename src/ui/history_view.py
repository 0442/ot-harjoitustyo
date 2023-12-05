from tkinter import Tk, ttk, scrolledtext
from tkinter.constants import *

from ui.base_view import _View

class HistoryView(_View):
    def __init__(self,
                 root: Tk,
                 history: str|None,
                 handle_back=lambda: None) -> None:
        self._handle_back = handle_back

        if history is None:
            self._history = (
                "You must log in first to view you calculation history."
            )
        elif len(history) == 0:
            self._history = "..."
        else:
            self._history = history

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
