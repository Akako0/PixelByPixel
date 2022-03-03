import pygame
from setings import Json


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, file):
        print(file)
        super().__init__()
        self.image = pygame.image.load(Json.world_folder+file).convert()
        self.image = pygame.transform.scale(self.image, (Json.chunck_size*Json.user_json["pixel_size"], Json.chunck_size*Json.user_json["pixel_size"]))
        self.rect = self.image.get_rect(topleft = (pos[0] ,pos[1]))
        self.direction = pygame.math.Vector2(0, 0)
    def get_input (self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.direction.y = 8
        elif keys[pygame.K_s]:
            self.direction.y = -8
        else:
            self.direction.y = 0

        if keys[pygame.K_q]:
            self.direction.x = 8
        elif keys[pygame.K_d]:
            self.direction.x = -8
        else:
            self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y