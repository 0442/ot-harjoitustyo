from typing import NamedTuple


class User(NamedTuple):
    """Represents a user.

    Attributes:
        username (str): The username of the user.
        state (Matrix): The password of the user.
    """

    username: str
    password: str
