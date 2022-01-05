import pygame as pg
import sprites
from settings import *

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Card Game")

playing = True

# bg_image = pg.image.load

card = sprites.SpriteSheet("Assets/deck_of_cards.png")
x_margin = 12
y_margin = 2
x_pad = 22
y_pad = 4

ace_hrts = card.image_at(9, 2, 44, 59)
# card_list = card.load_grid_images(4, 14, x_margin, x_pad, y_margin, y_pad)
# print(card_list)

clock = pg.time.Clock()

while playing:

   clock.tick(FPS)

   for event in pg.event.get():
       if event.type == pg.QUIT:
           playing = False
       if event.type == pg.KEYDOWN:    # allow for q key to quit the game
           if event.key == pg.K_q:
               playing == False

   screen.fill(BLACK)

   screen.blit(ace_hrts, (100, 100))

   pg.display.flip()

pg.quit()
