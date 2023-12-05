from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from calculator.calculator_service import CalculatorService
from ui.calculator_view import CalculatorView
from ui.login_view import LoginView
from ui.history_view import HistoryView
from ui.base_view import _View


class UI:
    def __init__(self, root: Tk) -> None:
        self._root: Tk = root
        self._current_view: _View = None
        self._calculator = CalculatorService()
        self._user = None

    def _close_current_view(self):
        self._current_view.close()

    def _open_main_view(self):
        if self._current_view:
            self._close_current_view()
        self._current_view = MainView(self._root,
                                      self._open_login_view,
                                      self._open_history_view)
        self._current_view.pack()

    def _open_history_view(self):
        ...

    def _open_login_view(self):
        if self._current_view:
            self._close_current_view()
        self._current_view = LoginView(self._root, self._open_main_view)
        self._current_view.pack()


    def start(self):
        self._open_main_view()

window = Tk()
window.title("Matriisilaskin")

ui = UI(window)
ui.start()

window.mainloop()