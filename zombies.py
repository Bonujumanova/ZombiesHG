import time

import pygame
import sys

pygame.init()
# screen settings directory
screen = pygame.display.set_mode((0, 0))
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  #screen.get_size()
COLOR_SKY_BLUE = (153, 204, 255)

#ZOMBIES PARAMETERS'
ZOMBIE_WIDTH: int = 120
ZOMBIE_HEIGHT: int = 200
BALD_ZOMBIE = pygame.image.load(
    "/home/bonu/Documents/zombies_hg/images/zombie_picture/bald_zombie.png"
)
BALD_ZOMBIE = pygame.transform.scale(
    BALD_ZOMBIE,
    (ZOMBIE_WIDTH, ZOMBIE_HEIGHT))
ZOMBIES_SPEED: int = 5
zombie_moving_right: bool = False
zombie_moving_left: bool = False
zombie_moving_up: bool = False
zombie_moving_down: bool = False
x_position: int = 100
y_position: int = 100

def zombie_moves_right(x: int) -> int:

    # temporary variable(speed)
    zombies_speed = 5
    x += zombies_speed
    return x

def zombie_moves_left(x: int) -> int:
    # speed
    zombiees_speed = 5
    x -= zombiees_speed
    return x


def zombie_moves_up(y: int) -> int:
    y -= 5
    return y


def zombie_moves_down(y: int) -> int:
    y += 5
    return y



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                zombie_moving_right = True
            elif event.key == pygame.K_LEFT:
                x_position = zombie_moves_left(x_position)
                zombie_moving_left = True
            elif event.key == pygame.K_UP:
                zombie_moving_up = True
            elif event.key == pygame.K_DOWN:
                zombie_moving_down = True
        elif event.type == pygame.KEYUP:
            zombie_moving_right: bool = False
            zombie_moving_left: bool = False
            zombie_moving_up: bool = False
            zombie_moving_down: bool = False



    if zombie_moving_left:
        x_position = zombie_moves_left(x_position)
    screen.fill(COLOR_SKY_BLUE)
    screen.blit(BALD_ZOMBIE, (x_position, 100))


    pygame.display.flip()
    time.sleep(1)