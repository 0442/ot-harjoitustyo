from entities.user import User
from entities.history_entry import HistoryEntry
from repositories.user_repository import UserRepository
from repositories.history_repository import HistoryRepository


class UserService:
    """High-level class which UI utilizes to perform user specific actions."""

    def __init__(self, user_repo: UserRepository, hist_repo: HistoryRepository) -> None:
        """Constructor for a UserService.

        Args:
            user_repo (UserRepository): A user repository object.
            hist_repo (HistoryRepository): A history repository object
        """
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

        hist = self._hist_repo.get_history(self._user.username)
        return "\n\n".join([str(h) for h in hist])

    def append_history(self, calculation: str, answer: str) -> None:
        """Append a calculation and its answer to currently
        logged in user's history.

        Args:
            calculation (str): The calculation performed.
            answer (str): The answer for the calculation.
        """
        if self._user is None:
            return

        entry = HistoryEntry(self._user.username, calculation, answer)
        self._hist_repo.append_history(entry)

    def log_in(self, login_user: User) -> tuple[bool, str | None]:
        """Attempts to log user in

        Args:
            username (str): User's username
            password (str): User's password

        Returns:
            tuple[bool, str|None]: Bool value indicates whether the login
            was successful. The str value contains an error message if
            the login failed and None if successful.
        """
        user = self._user_repo.find_user(login_user.username)
        if user is None or user.password != login_user.password:
            return False, "Invalid username or password"

        self._user = user
        return True, None

    def log_out(self) -> None:
        """Logs out the currently logged in user.
        """
        self._user = None

    def register(self, user: User) -> tuple[bool, str | None]:
        """Attempts to registers a new user.

        Args:
            username (str): Username for new user.
            password (str): Password for new user.

        Returns:
            tuple[bool, str|None]: Bool value indicates whether the login
            was successful. The str value contains an error message if
            the login failed and None if successful.
        """
        if len(user.username) < 3:
            return False, "Username must be at least 3 characters long."
        if len(user.password) < 3:
            return False, "Password must be at least 3 characters long."

        resp = self._user_repo.find_user(user.username)

        if resp is not None:
            return False, "Username already taken"

        success = self._user_repo.create_user(user)
        if not success:
            return False, "Failed to create account."

        return True, "Account registered. You can now try logging in."

    @property
    def user(self):
        return self._user
