import sys
import pygame as pg
from settings import *
from tiles import Tile
from level_top import Level

pg.init()
screen_width = 1200
screen_height = 700
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pg.display.update()
    clock.tick(60)