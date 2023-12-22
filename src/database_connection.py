from sqlite3 import connect, Connection, Row

from config import DB_FILE_PATH

connection: Connection = connect(DB_FILE_PATH)
connection.row_factory = Row
