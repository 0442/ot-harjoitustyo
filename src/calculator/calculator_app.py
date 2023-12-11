from re import sub

from calculator.utils.row_echelon import reduced_row_echelon
from calculator.utils.rational_number import Rn
from calculator.utils.matrix_utils import Matrix, Num

from repositories.user_repository import UserRepository, User
from repositories.history_repository import HistoryRepository


def str_to_num(num_str: str) -> Num:
    """Parses a string representing a number into a number.

    Args:
        num_str (str): A string representing a number.

    Returns:
        Num: The number (float, int, Rn) the string represents.

    Raises:
        ValueError if the format is invalid.
    """
    try:
        if num_str.count("/") == 1:
            rn = num_str.split("/")
            return Rn(int(rn[0]), int(rn[1]))

        if num_str.count(".") == 1:
            return float(num_str)

        return int(num_str)
    except ValueError:
        raise ValueError(f"Invalid number format: {num_str}")


def str_to_matrix(expression: str) -> Matrix:
    """Parses user written matrix expression into a matrix.

    Args:
        expression (str): A string representing a matrix. It can be formed using [], {} or ().

    Returns:
        Matrix: The matrix the expression represents.

    Raises:
        ValueError if the format is invalid.
    """
    expr = sub(r"\ +", r"", expression)
    expr = expr.strip(r"[](){},")

    if expr.count("],[") != 0:
        rows = expr.split(r"],[")
    elif expr.count("},{") != 0:
        rows = expr.split(r"},{")
    elif expr.count("),(") != 0:
        rows = expr.split(r"),(")
    else:
        rows = [expr]

    result = []
    for r in rows:
        nums = r.split(",")
        new_row = []
        for n in nums:
            new_row.append(str_to_num(n))
        result.append(new_row)

    return result


class App:
    """High-level class which UI utilizes to perform business logic."""

    def __init__(self, user_repo: UserRepository, hist_repo: HistoryRepository) -> None:
        self._user: User = None
        self._user_repo = user_repo
        self._hist_repo = hist_repo


    def find_row_reduce(self, expression: str) -> str:
        """Calculates the row reduces matrix from given expression if it is valid.

        Args:
            expression (str): _description_

        Returns:
            str: _description_
        """
        expression = str_to_matrix(expression)
        result = reduced_row_echelon(expression, [])
        return str(result)


    def get_history(self) -> list[str] | None:
        """Gets calulation history for logged in user.

        Returns:
            list[str] | None: Returns history of calculations if user is logged in, otherwise None.
        """
        if self._user is None:
            return None
        return []


    def log_in(self, username: str, password: str) -> tuple[bool, str|None]:
        """Attempts to log user in

        Args:
            username (str): User's username
            password (str): User's password

        Returns:
            tuple[bool, str|None]: Bool value indicates whether the login was successful. The str value contains an error message if the login failed and None if successful.
        """
        user = self._user_repo.find_user(username)
        if user is None:
            return False, "User not found"
        elif user.password == password:
            self._user = user
            return True, None
        else:
            return False, "Invalid username or password"


    def log_out(self) -> None:
        """Logs out the currently logged in user.
        """
        self._user = None


    def register(self, username: str, password: str) -> tuple[bool, str|None]:
        """Attempts to registers a new user.

        Args:
            username (str): Username for new user.
            password (str): Password for new user.

        Returns:
            tuple[bool, str|None]: Bool value indicates whether the login was successful. The str value contains an error message if the login failed and None if successful.
        """

        resp = self._user_repo.find_user(username)

        if resp is not None:
            return False, "Username already taken"

        self._user_repo.create_user(User(username, password))

        return True, "Account registered. You can try logging in."

    @property
    def user(self):
        return self._user
