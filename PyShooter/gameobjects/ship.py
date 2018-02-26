import pygame
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, game):
        super().__init__()
        self.game = game
        self.radius = radius
        self.x = x
        self.y = y
        self.angle = 0
        self.angularspeed = -0.001*math.pi

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        self.color = pygame.color.THECOLORS['yellow']
        self.hspeed = 0.15
        self.vspeed = 0.15
        self.boost = 1
        self.originalpoints = [(-20, 0), (0, -30), (20, 0), (0, 10)]
        self.points = self.originalpoints
        self.rotate()
        self.translate()
        self.pain = False
        self.onborder = False

        self.weapon = None
        self.shield = False

    def translate(self):
       self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def rotate(self):
        newPoints = []
        for x, y in self.originalpoints:
            newx = x * math.cos(self.angle) - y * math.sin(self.angle)
            newy = x * math.sin(self.angle) + y * math.cos(self.angle)
            newPoints.append((newx, newy))

        self.points = newPoints

    def startPain(self):
        self.color = pygame.color.THECOLORS['grey']
        self.pain = True

    def stopPain(self):
        self.color = pygame.color.THECOLORS['yellow']
        self.pain = False

    def startBoost(self, gamescene):
        if gamescene.boost > 0:
            gamescene.boost = gamescene.boost - 1
            self.boost = 2
            self.color = pygame.color.THECOLORS['orange']
        else:
            self.stopBoost()

    def stopBoost(self):
        self.boost = 1
        self.color = pygame.color.THECOLORS['yellow']

    def update(self, elapsed):
        self.onborder = False
        self.x += math.sin(self.angle) * self.vspeed * self.boost * elapsed 
        self.y += -math.cos(self.angle) * self.hspeed * self.boost * elapsed

        if self.x < 0:
            self.x = 0
            self.onborder = True
        if self.y < 0:
            self.y = 0
            self.onborder = True
        if self.x > self.game.width:
            self.x = self.game.width
            self.onborder = True
        if self.y > self.game.height:
            self.y = self.game.height
            self.onborder = True

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        self.points = self.originalpoints
        self.rotate()
        self.translate()
    
    def goLeft(self, elapsed):
        self.angle += self.angularspeed * elapsed

    def goRight(self, elapsed):
        self.angle += -self.angularspeed * elapsed

    def stop(self):
        pass

    def draw(self, screen):
        color = pygame.color.THECOLORS['yellow']
        pygame.draw.lines(screen, self.color, True, self.points, 5)