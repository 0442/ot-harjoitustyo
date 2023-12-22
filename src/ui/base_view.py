from tkinter import Tk, ttk
from tkinter.constants import *

from abc import ABC, abstractmethod


class BaseView(ABC):
    """Base class for a view

    Overwrite _layout() to define custom views for sub classes.
    """

    def __init__(self, root: Tk) -> None:
        self._root: Tk = root
        self._frame: ttk.Frame = None
        self._init_frame()
        self._layout()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root, padding="15 15 15 15")
        self._frame.grid(row=0, column=0, sticky=(N, S, E, W))
        self._frame.grid_propagate(True)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)

    def close(self):
        self._frame.destroy()

    def pack(self):
        self._frame.grid(row=0, column=0)

    @abstractmethod
    def _layout(self):
        pass

    @property
    def frame(self):
        return self._frame
