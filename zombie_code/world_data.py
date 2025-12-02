import pygame
from settings import Settings
class World:
    def __init__(self, data):
        # load image
        platform_block = pygame.image.load("/home/bonu/Documents/zombies_hg/images/Background/platform_block.bmp")
        self.settings = Settings()
# NOT finished
        # row_count = 0
        # for row in data:
        #     col_count = 0
        #     for tile in row:
        #         if tile == 1:
        #             img = pygame.transform.scale(platform_block, (self.settings.TILE_SIZE, self.settings.TILE_SIZE))
        #             img_rect = img.get_rect()
        #             img_rect .x = col_count * self.settings.TILE_SIZE
        #         col_count += 1
        #     row_count += 1