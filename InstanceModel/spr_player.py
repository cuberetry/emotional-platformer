import pygame
from pygame.locals import *
import GlobalVariable.game_var as gb_var
import GlobalVariable.sprite_group as gb_spr
from InstanceModel.System import spr_pause_menu as pause_menu

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.emotion_state = gb_var.EMOTION
        self.is_dead = False
        gb_spr.all_sprites.add(self)
        gb_spr.player_sprites.add(self)
        self.pause_menu = pause_menu.PauseMenu()

        # Rendering setup
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(gb_var.STATE_COLOR['n'])
        self.rect = self.surf.get_rect(center=(10, 420))

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
        if self.is_dead:
            if pressed_keys[K_SPACE]:
                self.respawn()
            return
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
        hit_platform = gb_spr.env_sprites
        self.rect.x += self.direction.x * self.speed
        for entity in hit_platform.sprites():
            if entity.rect.colliderect(self.rect):
                if entity in gb_spr.fire_sprites:
                    if self.emotion_state == 's':
                        entity.kill()
                    else:
                        self.player_kill()
                        return
                if entity in gb_spr.ice_sprites:
                    if self.emotion_state == 'a':
                        entity.kill()
                    else:
                        self.player_kill()
                        return
                if self.direction.x < 0:
                    self.rect.left = entity.rect.right
                elif self.direction.x > 0:
                    self.rect.right = entity.rect.left
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        for entity in hit_platform.sprites():
            if entity.rect.colliderect(self.rect):
                if entity in gb_spr.fire_sprites:
                    if self.emotion_state == 's':
                        entity.kill()
                    else:
                        self.player_kill()
                        return
                if entity in gb_spr.ice_sprites:
                    if self.emotion_state == 'a':
                        entity.kill()
                    else:
                        self.player_kill()
                        return
                if self.direction.y > 0:
                    self.rect.bottom = entity.rect.top
                    self.direction.y = 0
                    self.jumped = False
                elif self.direction.y < 0:
                    self.rect.top = entity.rect.bottom
                    self.direction.y = 0

        # Enemy collision
        hit_enemy = gb_spr.enemy_sprites
        for entity in hit_enemy.sprites():

            if entity.rect.colliderect(self.rect) and not self.emotion_state == 'w':
                self.player_kill()

        # Checkpoint collision
        hit_checkpoint = gb_spr.checkpoint_sprites
        for entity in hit_checkpoint.sprites():
            if entity.rect.colliderect(self.rect):
                entity.save_checkpoint()

        # Goal collision
        hit_goal = gb_spr.goal_sprites
        for entity in hit_goal.sprites():
            if entity.rect.colliderect(self.rect):
                entity.kill()
                self.reach_goal()

    # Update instance status
    def update(self):
        # Pausing
        if gb_var.IS_PAUSING:
            self.pause_menu.render_menu()
            return
        # Dead
        if self.is_dead:
            return

        # Player emotion state update
        self.emotion_state = gb_var.EMOTION
        if self.emotion_state == 'h':
            self.speed = 10
        else:
            self.speed = 5
        if self.emotion_state == 'w':
            self.surf.set_alpha(128)
        else:
            self.surf.set_alpha(None)
        self.surf.fill(gb_var.STATE_COLOR[self.emotion_state])

    def player_kill(self):
        self.surf.set_alpha(0)
        self.is_dead = True
        self.jumped = True

    def respawn(self):
        self.rect.x, self.rect.y = gb_var.CHECKPOINT
        self.direction = vec(0, 0)
        self.surf.set_alpha(None)
        self.is_dead = False

    @ staticmethod
    def reach_goal():
        print("Reached goal")
        exit(0)
