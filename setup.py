import sqlite3
import subprocess
import sys

subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
)


connection = sqlite3.connect("players.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE players ( name TEXT, score INTEGER);")
except Exception as e:
    print(e)

connection.commit()
connection.close()
