import pygame
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__()
        self.radius = radius
        self.x = x
        self.y = y
        self.angle = -math.pi / 2
        self.angularspeed = -0.001*math.pi

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        self.color = pygame.color.THECOLORS['yellow']
        self.hspeed = 0.15
        self.vspeed = 0.15
        self.boost = 1

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
        self.y += math.sin(self.angle) * self.vspeed * self.boost * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * self.boost * elapsed

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
    
    def goLeft(self, elapsed):
        self.angle += self.angularspeed * elapsed

    def goRight(self, elapsed):
        self.angle += -self.angularspeed * elapsed

    def stop(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        center = (int(self.x), int(self.y))
        px = int(self.x + 2 * self.radius * math.cos(self.angle))
        py = int(self.y + 2 * self.radius * math.sin(self.angle))
        pygame.draw.line(screen, self.color, center, (px, py))