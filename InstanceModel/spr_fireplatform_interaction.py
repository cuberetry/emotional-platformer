import pygame
import InstanceModel.spr_fire_platform as fire_p
import GlobalVariable.sprite_group as gb_spr


class FirePlatformHit:
    def __init__(self, player):
        self.player = player

    def hit(self):
        fire_platform = gb_spr.fire_sprites
        for entity in fire_platform.sprites():
            fire_hit = pygame.Rect.colliderect(entity.rect, self.player.rect)
            if fire_hit:
                print("hit")

