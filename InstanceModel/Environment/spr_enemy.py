import pygame
import GlobalVariable.game_var as gb_var
import GlobalVariable.sprite_group as gb_spr

vec = pygame.math.Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        gb_spr.all_sprites.add(self)
        gb_spr.enemy_sprites.add(self)

        # Rendering setup
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((0, 150, 75))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = x, y

        # Physic setup
        self.direction = vec(1, 0)
        self.speed = 1
        self.gravity = 0.8

    def draw(self, surface):
        surface.blit(self.surf, (self.rect.x, self.rect.y))

    # Update instance status
    def update(self):
        # Pausing
        if gb_var.IS_PAUSING:
            return

        # Movement and platform collision
        self.rect.x += self.direction.x * self.speed
        hit_platform = gb_spr.env_sprites
        for entity in hit_platform.sprites():
            if self.rect.colliderect(entity):
                self.direction.x = -self.direction.x
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        for entity in hit_platform.sprites():
            if self.rect.colliderect(entity):
                self.rect.bottom = entity.rect.top
                self.direction.y = 0
