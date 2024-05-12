import pygame as pg
import os
from random import randrange

from objects.game import Game
from .utils.utils import getRandomPos


class Player:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.getPos()  # type: ignore
        self.direction = pg.math.Vector2(0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

        pl_color = os.getenv("PL_COLOR")

        self.color = pl_color if pl_color != None else "green"


    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = pg.math.Vector2(0, -self.game.TILE_SIZE)
                self.directions = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = pg.math.Vector2(0, self.game.TILE_SIZE)
                self.directions = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = pg.math.Vector2(-self.game.TILE_SIZE, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}

            if event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = pg.math.Vector2(self.game.TILE_SIZE, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.launch()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.launch()

    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = getRandomPos(self.game.WINDOW_SIZE, self.game.TILE_SIZE) # type: ignore
            self.length += 1

    def check_selfeating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.launch()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length :]

    def draw(self):
        [pg.draw.rect(self.game.screen, self.color, segment) for segment in self.segments]

    def getPos(self):
        return getRandomPos(self.game.WINDOW_SIZE, self.game.TILE_SIZE)

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()
