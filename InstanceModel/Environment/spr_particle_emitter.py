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
                if p[4] == 'Circle':
                    pygame.draw.circle(gb_var.SURFACE, p[3],
                                       p[0], int(p[1]))

    def add_particles(self, x, y, amount=1, ptype='Jump'):
        c_list = ['blue', 'purple', 'green', 'orange',
                  'red', 'yellow', 'white']
        if ptype == 'Jump':
            radius = r.randint(5, 7)
            dir_x = r.randint(-5, 5)
            dir_y = r.randint(0, 5)
            color = 'White'
            shape = 'Circle'
        elif ptype == 'Death':
            radius = 4
            dir_x = r.randint(-5, 5)
            dir_y = r.randint(-5, 5)
            color = 'White'
            shape = 'Circle'
        elif ptype == 'Ice':
            radius = 4
            dir_x = r.randint(-5, 5)
            dir_y = r.randint(-5, 5)
            color = 'skyblue'
            shape = 'Circle'
        elif ptype == 'Fire':
            radius = 4
            dir_x = -1
            dir_y = r.randint(-5, 5)
            shape = 'Circle'
            color = 'darkorange'
        else:
            radius, dir_x, dir_y = 1, 1, 1
            color = "White"
            shape = "Circle"
        for p in range(amount):
            particle_circle = [[x, y], radius, [dir_x, dir_y], color, shape]
            self.particles.append(particle_circle)

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[1] > 0]
