import pygame
import sys

pygame.init()
# screen settings directory
screen = pygame.display.set_mode((0, 0))
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  #screen.get_size()
COLOR_SKY_BLUE: tuple[int, int, int] = (153, 204, 255)

clock = pygame.time.Clock()
fps: int = 60


#ZOMBIES PARAMETERS
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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        x_position  -= ZOMBIES_SPEED
    elif pressed_keys[pygame.K_RIGHT]:
        x_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_DOWN]:
        y_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_UP]:
        y_position -= ZOMBIES_SPEED


    screen.fill(COLOR_SKY_BLUE)
    screen.blit(BALD_ZOMBIE, (x_position, y_position))

    clock.tick(fps)
    pygame.display.flip()
