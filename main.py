import pygame as pg
import sprites
from settings import *
from sprites import Blocks

pg.init()

# Set Base Screen
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("platformer")

# sprite groups
blocks_group = pg.sprite.Group()

# testblock = Blocks("Assets/")
# blocks_group.add(testblock)

playing = True

platforms = sprites.SpriteSheet("Assets/OpenGunnerStarterTiles.png")
x_margin = 21
y_margin = 206
x_pad = 4
y_pad = 4
width = 50
height = 50

blocks = platforms.load_grid_images(3, 3, x_margin, x_pad, y_margin, y_pad, width, height)

clock = pg.time.Clock()

while playing:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
           playing = False
        if event.type == pg.KEYDOWN:    # allow for q key to quit the game
            if event.key == pg.K_q:
                playing = False

    screen.fill(BLACK)

    # blocks_group.draw(screen)
    screen.blit(blocks[0], (100, 100))

    pg.display.flip()

pg.quit()
