import pygame, sys
from pygame import K_SPACE

from bullet import Bullet
# from player import Player
from pathlib import Path
from player import Player
from settings import Settings
from world_data import World



class ZombieHG:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # передается кортеж (ширина, высота)
        # self.screen = (pygame.display.set_mode(
        #     (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT)))
        #color
        self.COLOR_SKY_BLUE: tuple[int, int, int] = (153, 204, 255)

        # # Fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        print(self.settings.SCREEN_HEIGHT, self.settings.SCREEN_WIDTH, "screewn h, w")
        # no FULLSCREEN
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.background_image = pygame.image.load(Path("/home/bonu/Documents/zombies_hg/images/platformer_assets/img/sky.png"))
        self.settings.SCREEN_WIDTH = self.screen.get_rect().width
        self.settings.SCREEN_HEIGHT = self.screen.get_rect().height
        self.world_data = World(self.settings.WORLD_DATA, self.screen)
        pygame.display.set_caption("Zombie HG")
        self.player = Player(self.screen, self.settings, self.world_data)
        self.bullets = pygame.sprite.Group()
        # time
        self.clock = pygame.time.Clock()
        self.fps = 60



    def run_game(self):
        while True:
            self.clock.tick(self.fps)

            self._check_events()
            self.player.update()
            self._update_bullets()
            self._update_screen()




    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
        # Move to right
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.player.jumping = True




    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False


    def _fire_bullet(self):
        """ создание новой пули и включение его в группу bullets"""
        if len(self.bullets) < self.settings.BULLET_ALLOWED:
            self.new_bullet = Bullet(self.screen, self.settings, self.player)
            self.bullets.add(self.new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        # Обновление позиций снарядов
        self.bullets.update()

        # Удаление снарядов, вышедших за экран
        for bullet in self.bullets.copy():
            if bullet.rect.x <= 0:
                self.bullets.remove(bullet)



    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.COLOR_SKY_BLUE)
        self.screen.blit(self.background_image, (0, 0))

        self.world_data.blit_platform_block()
        self.player.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Рисует сетку
        # self._draw_grid()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


    def _draw_grid(self):
        tile_size = self.settings.TILE_SIZE
        for line in range(self.settings.LINES_QUANTITY):
            pygame.draw.line(self.screen, (0, 0, 0), (0, line * tile_size),
                             (self.settings.SCREEN_WIDTH * tile_size, 0))
            pygame.draw.line(self.screen, (0, 0, 0),(line * tile_size, 0),
                             (line * tile_size, self.settings.SCREEN_HEIGHT))
        print("LINES_QUANTITY:", self.settings.LINES_QUANTITY)

    def _show_blocks(self):
        for tile in self.world_data.tile_list:
            self.screen.blit(tile[0], tile[1])




if __name__ == '__main__':
    z_hg = ZombieHG()
    z_hg.run_game()


