from sqlite3 import Connection

from database_connection import connection


class HistoryRepository:
    def __init__(self, db_connection: Connection) -> None:
        """
        Args:
            connection (Connection): sqlite3 database connection.
        """
        self._db_connection = db_connection

    def create_user(self):
        ...

    def delete_user(self):
        ...


history_repository = HistoryRepository(connection)


