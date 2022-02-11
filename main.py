import pygame as pg
import sprites
from settings import *

pg.init()

# Set Base Screen
pg.display.set_caption("platformer")

level1 = sprites.Layout1()
layout_list = level1.get_layout()
player = sprites.Player(75, 75, 25, layout_list)

playing = True

clock = pg.time.Clock()

while playing:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:    # allow for q key to quit the game
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
           playing = False

    SCREEN.fill(BLUE)

    level1.update()
    player.update()

    pg.display.flip()

pg.quit()
