import pygame
import random
import math

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = random.randint(9, 20) / 2
        self.npoints = 16
        self.points = []
        self.getPoints()
        self.color = pygame.color.THECOLORS['yellow']

    def getPoints(self):
        self.points = []
        for i in range(0, self.npoints):
            a = i / self.npoints  * math.pi * 2
            r = self.radius
            p = (r * math.sin(a) +  self.x, r * math.cos(a) + self.y)
            self.points.append(p)

    def update(self, elapsed):
        self.radius += 0.05 * elapsed
        self.getPoints()

    def draw(self, screen):
        for x, y in self.points:
            pygame.draw.rect(screen, self.color, (x, y, 2, 2))
