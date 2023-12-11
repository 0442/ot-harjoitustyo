from database_connection import connection, Connection


def init_db(db_conn: Connection) -> None:
    """Initializes the database.

    Args:
        connection (Connection): sqlite3 database connection.
    """

    cursor = db_conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS history;")

    cursor.execute(
        """
        CREATE TABLE users (
            username text primary key,
            password text
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE history (
            expression text primary key,
            username text,
            FOREIGN KEY(username) REFERENCES users(username)
        )
        """
    )

    db_conn.commit()


if __name__ == "__main__":
    init_db(connection)
