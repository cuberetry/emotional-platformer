import pygame
import GlobalVariable.sprite_group as gb_spr

vec = pygame.math.Vector2


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        gb_spr.all_sprites.add(self)
        gb_spr.env_sprites.add(self)

        # Rendering setup
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(width/2, height-10))
