from datetime import date
from .Model import Model
import sqlite3

DB_FILE = "entries.db"


class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from quotes")
        except sqlite3.OperationalError:
            cursor.execute(
                "create table quotes (quote text, author text, date date, type text, source text, rating float)"
            )
        cursor.close()

    def select(self):
        pass

    def insert(self):
        pass
