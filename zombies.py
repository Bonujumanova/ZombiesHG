import pygame
import sys

pygame.init()
# screen settings directory
screen = pygame.display.set_mode((0, 0))
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
print(SCREEN_WIDTH, SCREEN_HEIGHT)
COLOR_SKY_BLUE: tuple[int, int, int] = (153, 204, 255)
FIELD: int = 90
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
x_position: int = 100
y_position: int = 100

vertical_velocity: int = 0
gravity: int = 1

#
#Логика с прыжком пока не понятна, тк не знаю там будут препятствия либо платформы
# нужно понять каким будет конечный y
# def zombie_jumping(y: int, vertical_speed: int) -> int:
#
#     if vertical_speed < 30:
#         vertical_speed += gravity
#         y -= vertical_speed
#     else:
#         y = 100
#         vertical_speed = 0
#     return y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        if x_position > 0:
            x_position  -= ZOMBIES_SPEED
    elif pressed_keys[pygame.K_RIGHT]:
        if x_position< SCREEN_WIDTH - ZOMBIE_WIDTH:
            x_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_DOWN]:
        if y_position < SCREEN_HEIGHT - ZOMBIE_HEIGHT - FIELD:
            y_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_UP]:
        if y_position > 0:
            y_position -= ZOMBIES_SPEED
    # elif pressed_keys[pygame.K_SPACE]:
    #     vertical_velocity -= 10
    #     y_position= zombie_jumping(y_position, vertical_velocity)




    screen.fill(COLOR_SKY_BLUE)
    screen.blit(BALD_ZOMBIE, (x_position, y_position))

    clock.tick(fps)
    pygame.display.flip()
