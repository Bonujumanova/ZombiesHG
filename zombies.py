import pygame
import sys

pygame.init()
# screen settings directory
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
COLOR_SKY_BLUE = (153, 204, 255)

while True:

    screen.fill(COLOR_SKY_BLUE)
    pygame.display.flip()
