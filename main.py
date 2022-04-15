import pygame
import sprites
from settings import *

# base game elements
pg.init()
SCREEN = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("Platformer")

game_layout = sprites.Layout(LAYOUT)
layout_list = game_layout.get_layout()

player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()


player = sprites.Player(225, 525, 25, layout_list, game_layout.enemies)
player_group.add(player)


class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(BULLET_COLOR)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, BULLET_WIDTH, BULLET_HEIGHT])

        self.x_velo = 12

    def directional_firing(self):
        if self.rect.x > player.rect.centerx:
            self.rect.x += self.x_velo
        if self.rect.x < player.rect.centerx:
            self.rect.x -= self.x_velo

    def update(self):
        self.directional_firing()


def reset_level(new_level):
    global player, player_group, game_layout, layout_list
    # empty groups
    player_group.empty()
    game_layout.enemies.empty()
    player_bullet_group.empty()

    # create level
    game_layout.create(new_level)
    layout_list = game_layout.get_layout()
    player_group = pygame.sprite.Group()
    player = sprites.Player(225, 525, 25, layout_list, game_layout.enemies)
    player_group.add(player)

    return layout_list


def game_play():

    enemy_hits = 0
    level = 1
    max_level = 2

    layout_lis = reset_level(level)

    running = True

    clock = pg.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:    # allow for q key to quit the game
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pygame.K_e:
                    if player.left:
                        bullet = Shoot(player.rect.centerx - 27,
                                       player.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT)
                        player_bullet_group.add(bullet)
                    if player.right:
                        bullet = Shoot(player.rect.centerx + 20,
                                       player.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT)
                        player_bullet_group.add(bullet)
            if event.type == pg.QUIT:
                running = False

            # door collision
        for tile in layout_lis:
            if tile[1].colliderect(player.rect.x + 3, player.rect.y,
                                   player.rect.width, player.rect.height) and len(tile) == 3:
                level += 1

                if level <= max_level:

                    layout_lis = reset_level(level)

                else:
                    running = False

        SCREEN.fill(BLUE)

        player_group.update(SCREEN)
        game_layout.update(SCREEN)
        player_bullet_group.update()
        player_bullet_group.draw(SCREEN)

        pg.display.flip()

    pg.quit()


playing = True
while playing:
    game_play()

pg.quit()
