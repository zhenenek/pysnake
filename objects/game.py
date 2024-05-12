import os
from dotenv import load_dotenv
import pygame as pg


class Game:
    def __init__(self) -> None:
        pg.init()
        load_dotenv()

        self.WINDOW_SIZE = int(os.getenv("WIN_SIZE"))

        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
