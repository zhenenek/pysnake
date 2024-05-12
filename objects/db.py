__all__ = ["connection", "cursor"]
import sqlite3

connection = sqlite3.connect("players.db")
cursor = connection.cursor()
