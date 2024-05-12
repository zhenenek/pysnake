import sys
import sqlite3

from objects.db import *

from objects.game import Game


if __name__ == "__main__":
    # sys.path.append("..")

    name = sys.argv[1]

    cursor.execute(
        "INSERT OR IGNORE INTO players (name, score, length)  VALUES (?, 0, 1);",
        (name,),
    )
    try:
        connection.commit()
    except:
        ...

    cursor.execute(
        "SELECT name, score FROM players WHERE score = (SELECT MAX(score) FROM players);"
    )
    result = cursor.fetchone()

    if result:
        record_name, record = result
    else:
        record_name, record = "", 0

    game = Game(name, {"val": int(record), "name": record_name})
    game.run()

    connection.close()
