from random import randrange


def getRandomPos(win_size: int, tile_size: int):
    return [
        randrange(
            tile_size // 2,
            win_size - tile_size // 2,
            tile_size,
        )
    ] * 2
