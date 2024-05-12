# import sys
import sqlite3

from objects.game import Game


if __name__ == "__main__":
    # sys.path.append("..")

    connection = sqlite3.connect("players.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE players ( name TEXT, score INTEGER, length SMALLINT);")

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

    game = Game()
    game.run()
