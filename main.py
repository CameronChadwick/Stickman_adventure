import pygame as pg
import pygame.sprite

from sprites import *
from settings import *

pg.init()

# Set Base Screen
pg.display.set_caption("Platformer")

level1 = Layout()
layout_list = level1.get_layout()
bg_list = level1.get_bg()
enemies = level1.get_enemies()
player = Player(210, 550, 25, layout_list, enemies, bg_list)

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
