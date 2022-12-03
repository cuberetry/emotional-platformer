import pygame
from GlobalVariable import sprite_group as gb_spr


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Rendering setup
        self.cur_color = [255, 0, 0]
        self.cur_color_p = 2
        self.increasing = True
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(self.cur_color)
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = x, y

        # Add to sprite groups
        gb_spr.all_sprites.add(self)
        gb_spr.goal_sprites.add(self)

    def update(self):
        if self.cur_color[self.cur_color_p] < 255 and self.increasing:
            self.cur_color[self.cur_color_p] += 1
        elif self.cur_color[self.cur_color_p] > 0 and not self.increasing:
            self.cur_color[self.cur_color_p] -= 1
        else:
            self.cur_color_p += 1
            if self.cur_color_p == 3:
                self.cur_color_p = 0
            if self.cur_color[self.cur_color_p] == 255:
                self.increasing = False
            elif self.cur_color[self.cur_color_p] == 0:
                self.increasing = True
        self.surf.fill(self.cur_color)
