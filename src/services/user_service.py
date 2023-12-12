from repositories.user_repository import UserRepository, User
from repositories.history_repository import HistoryRepository

class UserService:
    def __init__(self, user_repo: UserRepository, hist_repo: HistoryRepository) -> None:
        """High-level class which UI utilizes to access user specific data."""
        self._user: User = None
        self._user_repo = user_repo
        self._hist_repo = hist_repo

    def get_history(self) -> list[str] | None:
        """Gets calulation history for logged in user.

        Returns:
            list[str] | None: Returns history of calculations if user is
            logged in, otherwise None.
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
            tuple[bool, str|None]: Bool value indicates whether the login
            was successful. The str value contains an error message if
            the login failed and None if successful.
        """
        user = self._user_repo.find_user(username)
        if user is None or user.password != password:
            return False, "Invalid username or password"

        self._user = user
        return True, None


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
            tuple[bool, str|None]: Bool value indicates whether the login
            was successful. The str value contains an error message if
            the login failed and None if successful.
        """

        resp = self._user_repo.find_user(username)

        if resp is not None:
            return False, "Username already taken"

        self._user_repo.create_user(User(username, password))

        return True, "Account registered. You can try logging in."

    @property
    def user(self):
        return self._user
