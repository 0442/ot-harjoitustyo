from tkinter import Tk, ttk
from tkinter.constants import *

class _View:
    """Base class for a view

    Overwrite _layout() to define custom views for sub classes.
    """
    def __init__(self, root:Tk) -> None:
        self._root:Tk = root
        self._frame:ttk.Frame = None
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

class MatrixCalculator(_View):
    def _layout(self):
        input_label = ttk.Label(master=self._frame, text="Expression")
        expr_input = ttk.Entry(master=self._frame)

        empty = ttk.Separator(master=self._frame)
        empty.grid(row=0, column=0)

        input_label.grid(row=0, column=0)
        expr_input.grid(row=0, column=1)

        self._root.grid_columnconfigure(1, minsize=300)

class EchelonCalculator(_View):
    def _layout(self):
        input_label = ttk.Label(master=self._frame, text="Expression")
        expr_input = ttk.Entry(master=self._frame)

        input_label.grid(row=0, column=0)
        expr_input.grid(row=0, column=1)

        self._root.grid_columnconfigure(1, minsize=300)

class MainView(_View):
    def __init__(self,
                 root: Tk,
                 nav_login = lambda: None,
                 nav_hist = lambda: None) -> None:
        self._nav_login = nav_login
        self._nav_hist = nav_hist
        super().__init__(root)

    def _layout(self):
        page_label = ttk.Label(master=self._frame, text="Home")
        heading = ttk.Label(master=self._frame, text="Calculators")
        login_button = ttk.Button(master=self._frame,
                                  text="Log in",
                                  command=self._nav_login)
        hist_button = ttk.Button(master=self._frame,
                                 text="History",
                                 command=self._nav_hist)
        sep = ttk.Separator(self._frame)

        tabs_cont = ttk.Notebook(master=self._frame)
        matrix_calc = MatrixCalculator(tabs_cont)
        echelon_calc = EchelonCalculator(tabs_cont)
        tabs_cont.add(child=matrix_calc.frame, text="Matrix calculator")
        tabs_cont.add(child=echelon_calc.frame, text="Row echelon calculator")


        page_label.grid(row=0, column=0, sticky=(W, N))
        login_button.grid(row=0, column=1)
        hist_button.grid(row=0, column=2)

        sep.grid(row=1, columnspan=2, sticky=(W,E))

        heading.grid(row=2, column=0, sticky=(W,E), pady=20)

        tabs_cont.grid(row=3, column=0)

        #self._root.grid_columnconfigure(0, weight=1, minsize=500)
        #self._root.grid_rowconfigure(0, weight=1, minsize=500)

class LoginView(_View):
    def __init__(self,
                 root: Tk,
                 handle_back = lambda: None,
                 handle_login = lambda : None) -> None:
        self._handle_back = handle_back
        self._handle_login = handle_login
        super().__init__(root)

    def _layout(self):
        back_button = ttk.Button(master=self._frame,
                                 text="Back",
                                 command=self._handle_back)
        back_button.grid(row=0, column=0, sticky=(N,W))

        box = ttk.LabelFrame(master=self._frame, text="Log in", padding="15 15 15 15")
        box.grid(row=1, column=0, sticky=(NW,SE))

        username_label = ttk.Label(master=box, text="Username")
        username_input = ttk.Entry(master=box)

        password_label = ttk.Label(master=box, text="Password")
        password_input = ttk.Entry(master=box)

        submit_button = ttk.Button(master=box,
                                   text="Log in",
                                   command=self._handle_login)

        username_label.grid(row=3, column=0, sticky=(W), pady=5)
        username_input.grid(row=3, column=1, sticky=(W,E), pady=5)

        password_label.grid(row=4, column=0, sticky=(W), pady=5)
        password_input.grid(row=4, column=1, sticky=(W,E), pady=5)

        submit_button.grid(row=5, column=0)

        box.grid_columnconfigure(1, minsize=300)

class UI:
    def __init__(self, root: Tk) -> None:
        self._root: Tk = root
        self._current_view:_View = None

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