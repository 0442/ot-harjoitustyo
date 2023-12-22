from sqlite3 import Connection

from entities.history_entry import HistoryEntry
from database_connection import connection


class HistoryRepository:
    def __init__(self, db_connection: Connection) -> None:
        """
        Args:
            connection (Connection): sqlite3 database connection.
        """
        self._db_connection = db_connection

    def get_history(self, username: str) -> list[HistoryEntry]:
        """Gets history for user with given username.

        Args:
            username (str): Username of the user for which to get the history.
        """
        cursor = self._db_connection.cursor()
        results = cursor.execute(
            "SELECT username, calculation, answer FROM history WHERE username = ?", (username,))
        results = results.fetchall()

        hist = []
        for r in results:
            hist.append(HistoryEntry(r[0], r[1], r[2]))

        return hist

    def append_history(self, entry: HistoryEntry):
        """Append a calculation with its answer to given user's history.

        Args:
            username (str): Username of the user for whom to add the entry.
            calculation (str): The calculation.
            answer (str): The answer of the calculation.
        """

        cursor = self._db_connection.cursor()
        cursor.execute("""
            INSERT INTO history (calculation, answer, username) VALUES (?,?,?)
        """, (entry.calculation, entry.answer, entry.username))

        self._db_connection.commit()

    def clear_database(self) -> None:
        """Deletes all history data from thedatabase.
        """
        cursor = self._db_connection.cursor()
        cursor.execute("DELETE FROM history")
        self._db_connection.commit()


history_repository = HistoryRepository(connection)
