import pygame
import GlobalVariable.sprite_group as gb_spr

vec = pygame.math.Vector2


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        gb_spr.all_sprites.add(self)
        gb_spr.env_sprites.add(self)

        # Rendering setup
        self.surf = pygame.Surface((16, 16))
        self.surf.fill(gb_var.PLATFORM_STATE_COLOR['pp'])
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.surf, (self.rect.x, self.rect.y))


