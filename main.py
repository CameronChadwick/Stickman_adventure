import pygame as pg
import pygame.sprite

from sprites import *
from settings import *

pg.init()

# Set Base Screen
pg.display.set_caption("Platformer")

bullet_group = pygame.sprite.Group()
enemy_hits = 0
level = 1
max_level = 2

player_group = pygame.sprite.GroupSingle()

game_layout = Layout()
layout_list = game_layout.get_layout()


player = Player(150, 600, 25, layout_list, game_layout.enemies)
player_group.add(player)


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

    def directional_firing(self):
        if self.rect.x > player.rect.centerx:
            self.rect.x += self.x_velo
        if self.rect.x < player.rect.centerx:
            self.rect.x -= self.x_velo

    def update(self):
        self.directional_firing()


playing = True

clock = pg.time.Clock()

while playing:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:    # allow for q key to quit the game
            if event.key == pg.K_ESCAPE:
                playing = False
            if event.key == pygame.K_e:
                if player.left:
                    bullet = Shoot(player.rect.centerx - 27,
                                   player.rect.top + 17)
                    bullet_group.add(bullet)
                if player.right:
                    bullet = Shoot(player.rect.centerx + 20,
                                   player.rect.top + 17)
                    bullet_group.add(bullet)
        if event.type == pg.QUIT:
            playing = False
# enemy collision
    enemyhit = pygame.sprite.groupcollide(bullet_group, game_layout.enemies, True, True)

# door collision
    for tile in game_layout.tile_list:
        if tile[1].colliderect(player.rect.x + 3, player.rect.y,
                                player.rect.width, player.rect.height) and len(tile) == 3:
            pass

    SCREEN.fill(BLUE)

    game_layout.update()
    player.update()
    bullet_group.update()
    bullet_group.draw(SCREEN)

    pg.display.flip()

pg.quit()
