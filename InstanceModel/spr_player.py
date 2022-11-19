import pygame
from pygame.locals import *
import GlobalVariable.game_var as gb_var
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, acc_rate=gb_var.ACCELERATION):
        super().__init__()
        self.emotion_state = gb_var.EMOTION
        gb_spr.all_sprites.add(self)
        gb_spr.player_sprites.add(self)

        # Rendering setup
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(gb_var.STATE_COLOR['n'])
        self.rect = self.surf.get_rect(center=(10, 420))

        # Physic setup
        self.acc_rate = acc_rate
        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumped = False

    # Simple movement
    def move(self):
        self.acc = vec(0, 0.5)
        # Input handling and movement logic
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -self.acc_rate
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = self.acc_rate
        if pressed_keys[K_SPACE] and self.vel.y == 0 and not self.jumped:
            self.jumped = True
            self.vel.y = -15

        if self.jumped:
            if self.vel.y > 0:
                self.jumped = False

        self.acc.x += self.vel.x * gb_var.FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > gb_setting.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = gb_setting.WIDTH

        self.rect.midbottom = self.pos

    # Update instance status
    def update(self):
        # Player emotion state update
        self.emotion_state = gb_var.EMOTION
        self.surf.fill(gb_var.STATE_COLOR[self.emotion_state])

        # Collision detection
        hit_platform = pygame.sprite.spritecollide(self, gb_spr.env_sprites, False)
        if hit_platform:
            self.pos.y = hit_platform[0].rect.top + 1
            self.vel.y = 0
