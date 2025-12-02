import pygame

class Player:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        # загрузка изображения корабля и получение прямоугольника
        self.player_standing_image = (pygame.image.load
            ('/home/bonu/Documents/zombies_hg/images/Idle/zombie_alph2a.bmp'))
        self.image_width = self.player_standing_image.get_width()
        self.image_height = self.player_standing_image.get_height()

        self.scaled_image = (pygame.transform.scale
                (self.player_standing_image, (self.image_width // 3, self.image_height // 3)))
        self.rect = self.scaled_image.get_rect()
        # после смерти или при reset игрок появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # moving flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляет атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.PLAYER_SPEED
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.PLAYER_SPEED


    def blitme(self):
        """ Рисует игрока в текущей позиции."""
        self.screen.blit(self.scaled_image, self.rect)




