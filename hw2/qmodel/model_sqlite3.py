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
        """
        Gets all quotes from the database
        :return: List containing all quotes
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select * from quotes")
        return cursor.fetchall()

    def insert(self, quote, author, date, type, source, rating):
        """
        Inserts a quote into the database
        :param quote: String
        :param author: String
        :param date: String
        :param type: String
        :param source: String
        :param rating: float
        :return: None
        """
        params = {
            "quote": quote,
            "author": author,
            "date": date,
            "type": type,
            "source": source,
            "rating": rating,
        }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
            "insert into quotes (quote, author, date, type, source, rating) values (:quote, :author, :date, :type, :source, :rating)",
            params,
        )
        connection.commit()
        cursor.close()
        return True
