from os import getenv, path
from dotenv import load_dotenv

dirname = path.dirname(__file__)
load_dotenv(dotenv_path=path.join(dirname, "..", ".env"))

if getenv("TEST"):
    DB_FILE_PATH = "test_database.db"
else:
    DB_FILE_PATH = path.join(dirname, getenv("DB_FILE_PATH")) or "database.db"

LATEX_INDENT = getenv("LATEX_INDENT") or 4*" "
LATEX_MAT_BEGIN = getenv("LATEX_MAT_BEGIN") or r"\[\begin{bmatrix}"
LATEX_MAT_END = getenv("LATEX_MAT_END") or r"\end{bmatrix}\]"
