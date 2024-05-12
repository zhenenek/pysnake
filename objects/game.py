import os
from dotenv import load_dotenv
import pygame as pg


class Game:
    def __init__(self) -> None:
        pg.init()
        load_dotenv()

        win_size = os.getenv("WIN_SIZE")
        tile_size = os.getenv("TILE_SIZE")
        draw_rate = os.getenv("DRAW_RATE")

        self.WINDOW_SIZE = int(win_size) if win_size != None else 0
        self.TILE_SIZE = int(tile_size) if tile_size != None else 0
        self.DRAWING_RATE = int(draw_rate) if draw_rate != None else 0

        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()

    def draw_tiles(self):
        for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE):
            pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
        for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE):
            pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))

    def draw(self) -> None:
        self.screen.fill("black")
        self.draw_tiles()
        self.player.draw()
        # self.food.draw()

    def update(self) -> None:
        pg.display.flip()
        self.clock.tick(self.DRAWING_RATE)

    def event(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    def launch(self):

        from objects.player import Player

        self.player = Player(self)

        # self.food = Food(self)

    def run(self):
        self.launch()
        while True:
            self.event()
            self.update()
            self.draw()
