from tkinter import Tk, ttk
from tkinter.constants import *


class _View:
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
        self._frame.grid(row=0, column=0, sticky=(NW, SE))

    def close(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=X)

    def _layout(self): ...

    @property
    def frame(self):
        return self._frame
