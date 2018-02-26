import pygame
import random
import math
import gameobjects.texteffect

class Bonus(pygame.sprite.Sprite):
    def __init__(self, game, x, y, angle, scene):
        super().__init__()
        self.game = game
        self.scene = scene
        self.size = 10
        self.value = 1
        self.x = x - self.size / 2
        self.y = y - self.size / 2
        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vspeed = random.uniform(0.02, 0.06)
        self.hspeed = random.uniform(0.02, 0.06)
        self.angle = angle
        self.rotationAngle = random.uniform(0, math.pi / 2)
        angleoffset = random.uniform(0, math.pi / 6) - math.pi / 12
        self.angle += angleoffset

        self.originalpoints = ((0, 0), (10, 0), (10, 10), (0, 10))
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

        self.color = pygame.color.THECOLORS['red']

    def rotate(self):
        newPoints = []
        for x, y in self.originalpoints:
            newx = x * math.cos(self.rotationAngle) + y * math.sin(self.rotationAngle)
            newy = -x * math.sin(self.rotationAngle) + y * math.cos(self.rotationAngle)
            newPoints.append((newx, newy))

        return newPoints

    def effect(self):
        self.scene.score += self.value

    def getVisualEffect(self):
        e = gameobjects.texteffect.TextEffect("+{}".format(self.value), self.game)
        return e

    def update(self, elapsed):
        self.rotationAngle += -0.01*math.pi
        self.y +=  math.sin(self.angle) * self.vspeed * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * elapsed
        self.rect.x = self.x + self.size / 2
        self.rect.y = self.y + self.size / 2

        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

        if not self.inGame():
            self.kill()

    def inGame(self):
        return (self.x > 0 and self.x < self.game.width) and (self.y > 0 and self.y < self.game.height)

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points, 1)
