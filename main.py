import pygame as pg
import pygame.sprite

from sprites import *
from settings import *

pg.init()

# Set Base Screen
pg.display.set_caption("Platformer")

bullet_group = pygame.sprite.Group()


class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(BULLET_COLOR)
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, BULLET_WIDTH, BULLET_HEIGHT])

        self.x_velo = 12

    def update(self):
        # directional firing needs work
        if level1.player.left:
            self.rect.x -= self.x_velo
        elif level1.player.right:
            self.rect.x += self.x_velo


level1 = Layout()

playing = True

clock = pg.time.Clock()

while playing:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:    # allow for q key to quit the game
            if event.key == pg.K_ESCAPE:
                playing = False
            if event.key == pygame.K_e:
                bullet = Shoot(level1.player.rect.centerx,
                               level1.player.rect.top + 18)
                bullet_group.add(bullet)
        if event.type == pg.QUIT:
            playing = False

    SCREEN.fill(BLUE)

    level1.update()
    bullet_group.update()
    bullet_group.draw(SCREEN)

    pg.display.flip()

pg.quit()
