import pygame_menu as pgm
from GlobalVariable import game_var as gb_var
from PygamePage import scene0


class Scene:
    def __init__(self):
        # Create a simple menu with buttons
        self.menu = pgm.Menu('Emotional Platformer', 400, 300, theme=pgm.themes.THEME_DARK)
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Quit', pgm.events.EXIT)

    def mainloop(self):
        self.menu.mainloop(gb_var.SURFACE, disable_loop=True)

    def start_game(self):
        self.menu.disable()
        gb_var.CUR_SCENE = scene0.Scene()
