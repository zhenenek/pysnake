import sys
import sqlite3

from objects.db import *

from objects.game import Game


if __name__ == "__main__":
    # sys.path.append("..")

    name = sys.argv[1]

    cursor.execute(
        """INSERT INTO players (name, score)
SELECT ?, 0
WHERE NOT EXISTS (
    SELECT 1 FROM players WHERE name = ?
);
""",
        (name, name),
    )
    try:
        connection.commit()
    except:
        ...

    game = Game(name)
    game.run()

    connection.close()
