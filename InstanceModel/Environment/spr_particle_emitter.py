import pygame
import GlobalVariable.game_var as gb_var
import random as r


class ParticleEmitter:
    def __init__(self):
        self.particles = list()

    def emit(self):
        if self.particles:
            self.delete_particles()
            for p in self.particles:
                p[0][0] += p[2][0]
                p[0][1] += p[2][1]
                p[1] -= 0.2
                pygame.draw.circle(gb_var.SURFACE, pygame.Color('White'),
                                   p[0], int(p[1]))

    def add_particles(self, x, y):
        radius = r.randint(5, 7)
        dir_x = r.randint(-5, 5)
        dir_y = r.randint(0, 5)
        particle_circle = [[x, y], radius, [dir_x, dir_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[1] > 0]
