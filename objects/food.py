import pygame as pg
import os

from objects.game import Game
from .utils.utils import getRandomPos


class Food:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = getRandomPos(game.WINDOW_SIZE, game.TILE_SIZE)  # type: ignore

        fd_cost = os.getenv("FD_COST")

        self.cost = int(fd_cost) if fd_cost != None else 15

    def draw(self):
        pg.draw.rect(self.game.screen, "red", self.rect)
