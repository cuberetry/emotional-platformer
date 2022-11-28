import pygame
from pygame.locals import *
import GlobalVariable.game_var as gb_var
import GlobalVariable.game_setting as gb_setting
import GlobalVariable.sprite_group as gb_spr
from InstanceModel import spr_pause_menu as pause_menu

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, acc_rate=gb_var.ACCELERATION):
        super().__init__()
        self.emotion_state = gb_var.EMOTION
        gb_spr.all_sprites.add(self)
        gb_spr.player_sprites.add(self)
        self.pause_menu = pause_menu.PauseMenu()

        # Rendering setup
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(gb_var.STATE_COLOR['n'])
        self.rect = self.surf.get_rect(center=(10, 420))
        self.left_border, self.right_border = -50, 1450

        # Physic setup
        self.direction = vec(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.jumped = False

    # Simple movement
    def move(self):
        if gb_var.IS_PAUSING:
            return
        # Input handling
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            self.pause_menu.activate_menu()
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.direction.x = -1
        elif pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if pressed_keys[K_SPACE] and not self.jumped and self.direction.y == 0:
            self.jumped = True
            self.direction.y = self.jump_speed

        # Movement handling
        self.rect.x += self.direction.x * self.speed
        hit_platform = gb_spr.env_sprites
        for entity in hit_platform.sprites():
            if entity.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = entity.rect.right
                elif self.direction.x > 0:
                    self.rect.right = entity.rect.left
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        for entity in hit_platform.sprites():
            if entity.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = entity.rect.top
                    self.direction.y = 0
                    self.jumped = False
                elif self.direction.y < 0:
                    self.rect.top = entity.rect.bottom
                    self.direction.y = 0

    # Update instance status
    def update(self):
        # Pausing
        if gb_var.IS_PAUSING:
            self.pause_menu.render_menu()
            return

        # Player emotion state update
        self.emotion_state = gb_var.EMOTION
        self.surf.fill(gb_var.STATE_COLOR[self.emotion_state])
