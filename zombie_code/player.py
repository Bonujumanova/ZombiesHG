import pygame
from settings import Settings
from world_data import World

class Player:

    def __init__(self, screen, settings, world):
        self.screen = screen
        self.settings = settings
        self.world = world

        self.screen_rect = screen.get_rect()

        self.image_index = 0
        self.direction = 0
        self.image_width = 0
        self.image_height = 0

        self.player_running_right_images, self.player_running_left_images = self.animation()


        self.player_img = self.player_running_right_images[self.image_index]
        self.rect = self.player_img.get_rect()

        # после смерти или при reset игрок появляется у нижнего края экрана
        self.rect.y = self.settings.SCREEN_HEIGHT - (self.settings.TILE_SIZE + self.image_height)
        # последняя y позиция игрока, нужна для прыжков
        self.last_players_y_pos = self.rect.y
        # Сохранение вещественной координаты центра
        self.rect.x = self.rect.x + self.settings.TILE_SIZE
        self.x = float(self.rect.x)
        self.player_x = 0
        self.player_y = 0

        # moving flag
        self.moving_right = False
        self.moving_left = False
        self.jumping = False


    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        self.player_moving_right()
        self.player_moving_left()
        self.player_jumping()
        self.choosing_direction()
        self.players_pose_after_moving()




    def animation(self):
        player_running_right_images = []
        player_running_left_images = []
        for num in range(1, 12):
        # загрузка изображения и получение прямоугольника
            player_running_image = (pygame.image.load
                (f'/home/bonu/Documents/zombies_hg/images/Run Throwing/0_Skeleton_Crusader_Run Throwing_{num}.bmp'))
            self.image_width = player_running_image.get_width() // 3
            self.image_height = player_running_image.get_height() // 3

            right_side_img = (pygame.transform.scale
                    (player_running_image, (self.image_width , self.image_height)))
            left_side_img = pygame.transform.flip(right_side_img, True, False)

            player_running_right_images.append(right_side_img)
            player_running_left_images.append(left_side_img)

        return player_running_right_images, player_running_left_images


    def players_pose_after_moving(self):
        if self.moving_right == False and self.moving_left == False:
            self.image_index = 0

            if self.direction == 1:
                self.player_img = self.player_running_right_images[self.image_index]
            if self.direction == -1:
                self.player_img = self.player_running_left_images[self.image_index]

    def player_moving_right(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - self.settings.TILE_SIZE:
            self.rect.x += self.settings.PLAYER_SPEED
            self.direction = 1

    def player_moving_left(self):
        if self.moving_left and self.rect.left > self.settings.TILE_SIZE:
            self.rect.x -= self.settings.PLAYER_SPEED
            self.direction = -1

    def player_jumping(self):
        if not self.jumping:
            self.last_players_y_pos = self.rect.y
        if self.jumping:
            self.rect.y -= self.settings.GRAVITATION_FORCE
            self.settings.GRAVITATION_FORCE -= 1
            if self.rect.y == self.last_players_y_pos:
                self.settings.GRAVITATION_FORCE = 15
                self.jumping = False

    def choosing_direction(self):
        if self.moving_right or self.moving_left:
            self.image_index += 1
            if self.direction == 1:
                self.player_img = self.player_running_right_images[self.image_index]
            elif self.direction == -1:
                self.player_img = self.player_running_left_images[self.image_index]
            if self.image_index >= len(self.player_running_right_images) - 1:
                self.image_index = 0

    def collision_check(self):
        for tile in self.world.tile_list:

            # check collision in y direction
            if tile[1].colliderect(self.rect):
                # pygame.draw.rect(self.screen,
                #                  (150, 180, 255), self.rect, 2, 15)
                print(f"TAIL: {tile[1][2]}")




                self.rect.y = tile[1].y - self.image_height


                print("LOX")

    def blitme(self):
        """ Рисует игрока в текущей позиции."""
        self.screen.blit(self.player_img, self.rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2)
        self.collision_check()
        print(self.rect.y, "self.rect.y")




