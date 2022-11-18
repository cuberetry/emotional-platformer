import pygame

vec = pygame.math.Vector2


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(width/2, height-10))
