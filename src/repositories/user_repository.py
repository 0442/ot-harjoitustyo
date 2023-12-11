from typing import NamedTuple
from sqlite3 import Connection

from database_connection import connection


class User(NamedTuple):
    """Represents a user."""
    username: str
    password: str


class UserRepository:
    def __init__(self, db_connection: Connection) -> None:
        """
        Args:
            connection (Connection): sqlite3 database connection.
        """
        self._db_connection = db_connection

    def create_user(self, user: User) -> bool:
        """Creates a new user.

        Args:
            user (User): Object representing the user to be created.

        Returns:
            bool: True if successful, otherwise False.
        """

        cursor = self._db_connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO users (
                    username, password
                ) VALUES (?, ?)""",
                (user.username, user.password)
            )
        except:
            return False

        self._db_connection.commit()
        return True

    def find_user(self, username: str) -> User | None:
        """Finds and return a user.

        Args:
            user (str): User representing the user to be searched.

        Returns:
            str | None: Returns username if found, otherwise None.
        """

        cursor = self._db_connection.cursor()
        res = cursor.execute("""
            SELECT username, password
            FROM users
            WHERE username = ?""",
            (username,)
        ).fetchone()

        if res is None:
            return None

        user = User(res[0], res[1])
        return user

    def delete_user(self, user: User):
        """Deletes a user.

        Args:
            user (User): User representing the user to be deleted.
        """

        cursor = self._db_connection.cursor()
        cursor.execute("DELETE FROM users WHERE username = ? AND password = ?",
                       (user.username, user.password))

        self._db_connection.commit()


user_repository = UserRepository(connection)
