import pygame
import random
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(9, 20)
        self.image = pygame.Surface([self.radius, self.radius])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.radius)
        self.startX = self.rect.x
        self.rect.y = 0
        self.color = pygame.color.THECOLORS['red']
        self.verticalSpeed = random.uniform(0.095, 0.15)
        self.amplitude = random.randint(80, 120)
        if random.randint(1,2) == 1:
            self.movement = self.sinMovement
        else:
            self.movement = self.cosMovement

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x + self.radius, self.rect.y +  self.radius), self.radius)

    def update(self, elapsed, gameScene):
        self.rect.y += self.verticalSpeed * elapsed
        if self.rect.y > 600:
            self.kill()
            gameScene.missed += 1
        self.rect.x = self.movement()

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 800 - self.radius * 2:
            self.rect.x = 800 - self.radius * 2

    def sinMovement(self):
        return -1 * math.sin(self.rect.y / 50) * self.amplitude + self.startX

    def cosMovement(self):
        return -1 * math.cos(self.rect.y / 50) * self.amplitude + self.startX

class Explosion(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.x = enemy.rect.x
        self.y = enemy.rect.y
        self.radius = enemy.radius / 2
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

class Star():
    def __init__(self, x, y):
        self.x = x
        self.y = y
