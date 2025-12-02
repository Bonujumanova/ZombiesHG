import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Класс для управления пулями, выпущенными игроком."""

    def __init__(self, screen, settings, player):
        """Создает объект пуль в текущей позиции игрока"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.COLOR = self.settings.BULLET_COLOR

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.BULLET_WIDTH, self.settings.BULLET_HEIGHT)
        self.rect.midtop = player.rect.midtop

        # Позиция снарядов хранится в вещественном формате.
        self.x = float(self.rect.x)

    def update(self):
        """ Перемещает снаряд по горизонтали"""
        # Обновление позиции снаряда в вещественном формате
        self.x -= self.settings.BULLET_SPEED
        # Обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        """ Вывод пули на экран"""
        pygame.draw.ellipse(self.screen, self.COLOR, self.rect)



