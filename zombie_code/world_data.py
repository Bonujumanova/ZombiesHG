import pygame
from settings import Settings
class World:
    def __init__(self, data, screen):
        self.tile_list = []
        # load image
        brown_platform_block = pygame.image.load("/home/bonu/Documents/zombies_hg/images/Background/platform_block.bmp")
        dark_platform_block = pygame.image.load("/home/bonu/Documents/zombies_hg/images/Background/dark_block.bmp")
        sun = pygame.image.load("/home/bonu/Documents/zombies_hg/images/platformer_assets/img/sun.png")
        sky_background = pygame.image.load("/home/bonu/Documents/zombies_hg/images/platformer_assets/img/sky.png")
        self.screen = screen
        self.settings = Settings()

# NOT finished
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(brown_platform_block, (self.settings.TILE_SIZE, self.settings.TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.settings.TILE_SIZE
                    img_rect.y = row_count * self.settings.TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 2:
                    dark_img = pygame.transform.scale(dark_platform_block, (self.settings.TILE_SIZE, self.settings.TILE_SIZE))
                    img_rect = dark_img.get_rect()
                    img_rect.x = col_count * self.settings.TILE_SIZE
                    img_rect.y = row_count * self.settings.TILE_SIZE
                    tile = (dark_img, img_rect)
                    self.tile_list.append(tile)

                elif tile == 3:
                    dark_img = pygame.transform.scale(sun, (self.settings.TILE_SIZE, self.settings.TILE_SIZE))
                    img_rect = dark_img.get_rect()
                    img_rect.x = col_count * self.settings.TILE_SIZE
                    img_rect.y = row_count * self.settings.TILE_SIZE
                    tile = (dark_img, img_rect)
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1




    def blit_platform_block(self):

        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            pygame.draw.rect(self.screen, (255, 255, 255), tile[1], 2 )





