from tkinter import Tk, ttk, StringVar, IntVar
from tkinter.constants import *

from calculator.calculator_app import App
from repositories.user_repository import user_repository
from repositories.history_repository import history_repository

from ui.calculator_view import CalculatorView
from ui.login_view import LoginView
from ui.history_view import HistoryView
from ui.base_view import BaseView


class UI:
    def __init__(self, root: Tk, app: App) -> None:
        self._root: Tk = root
        self._current_view: BaseView = None
        self._app = app

    def _close_current_view(self):
        if self._current_view:
            self._current_view.close()

    def _open_main_view(self):
        self._close_current_view()
        self._current_view = CalculatorView(self._root,
                                            self._app,
                                            self._open_login_view,
                                            self._open_history_view)
        self._current_view.pack()

    def _open_login_view(self):
        if self._current_view:
            self._close_current_view()
        self._current_view = LoginView(self._root,
                                       self._app,
                                       self._open_main_view)
        self._current_view.pack()

    def _open_history_view(self):
        if self._current_view:
            self._close_current_view()
        self._current_view = HistoryView(self._root,
                                         self._app,
                                         self._open_main_view)
        self._current_view.pack()

    def start(self):
        self._open_main_view()


window = Tk()
window.title("Matriisilaskin")

calculator = App(user_repository, history_repository)
ui = UI(window, calculator)
ui.start()

window.mainloop()
