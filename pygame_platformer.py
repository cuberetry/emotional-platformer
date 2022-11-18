import sys
import pygame
from pygame.locals import *
from InstanceModel.spr_platform import *
from InstanceModel.spr_player import *

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emotional Platformer")

P1 = Player()
platform_1 = Platform(WIDTH, HEIGHT)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(platform_1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display_surface.fill((0, 0, 0))

    for entity in all_sprites:
        display_surface.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)