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
is_player_jumping: bool = False
y_last: int = 0
# гравитация - пока не дошел до нуля идет идет прыжок вврех,/
# когда гравитация равна нулю, y_position достигнет наивысшей точки в прыжки и затем начнет убавляться
# gravity становится отрицательным, поэтому происходит увеличение y_position
# пример, мяч подброшенный в воздух,с ускорением долетает до максимальной высоты, затем останавливается и
# стремится вниз( начинает падать вниз с ускорением) из-за сил гравитации
gravity: int = 15



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_player_jumping:
                    is_player_jumping = True
                    y_last = y_position

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        if x_position > 0:
            x_position  -= ZOMBIES_SPEED
    elif pressed_keys[pygame.K_RIGHT]:
        if x_position< SCREEN_WIDTH - ZOMBIE_WIDTH:
            x_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_DOWN] and not is_player_jumping:
        if y_position < SCREEN_HEIGHT - ZOMBIE_HEIGHT - FIELD:
            y_position += ZOMBIES_SPEED
    elif pressed_keys[pygame.K_UP] and not is_player_jumping:
        if y_position > 0:
            y_position -= ZOMBIES_SPEED
    if is_player_jumping:
        y_position -= gravity
        gravity -= 1

        if y_position == y_last:
            gravity = 15
            is_player_jumping = False




    screen.fill(COLOR_SKY_BLUE)
    screen.blit(BALD_ZOMBIE, (x_position, y_position))

    clock.tick(fps)
    pygame.display.flip()
