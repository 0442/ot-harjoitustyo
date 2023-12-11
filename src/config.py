from os import getenv, path
from dotenv import load_dotenv

dirname = path.dirname(__file__)
load_dotenv(dotenv_path = path.join(dirname, "..", ".env"))

DB_FILE_PATH = path.join(dirname, getenv("DB_FILE_PATH")) or "database.db"
