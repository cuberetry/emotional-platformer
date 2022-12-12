import os
import pygame

pygame.init()

MAXFPS = 60
HEIGHT = 450
WIDTH = 400
ROOT_PATH = "/".join(os.path.dirname(__file__).split("/")[:-1:])
FONT_GAME_OVER = pygame.font.Font('freesansbold.ttf', 24)
FONT_PRESS_SPACE = pygame.font.Font('freesansbold.ttf', 18)
