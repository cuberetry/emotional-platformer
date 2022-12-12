import pygame
from GlobalVariable import game_var as gb_var
from GlobalVariable import sprite_group as gb_spr


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

        # Rendering setup
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 175, 100))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        # Add to sprite groups
        gb_spr.all_sprites.add(self)
        gb_spr.checkpoint_sprites.add(self)

    def draw(self, surface):
        surface.blit(self.surf, (self.rect.x, self.rect.y))

    def save_checkpoint(self):
        gb_var.CHECKPOINT = [self.x, self.y]
        self.kill()
