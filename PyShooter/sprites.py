import pygame
import random
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.width = w
        self.height = h
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = pygame.color.THECOLORS['yellow']
        
        self.horizontalSpeed = 0

        self.pointA = (x, y)
        self.pointB = (x + w, y)
        self.pointC = (x + h/2, y - h)
    
    def update(self):
        if self.horizontalSpeed > 5:
            self.horizontalSpeed = 5
        if self.horizontalSpeed < -5:
            self.horizontalSpeed = -5
        self.rect.x += self.horizontalSpeed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 800 - self.width:
            self.rect.x = 800 - self.width

        ax, ay = self.pointA
        bx, by = self.pointB
        cx, cy = self.pointC
        newax = ax + self.horizontalSpeed
        newbx = bx + self.horizontalSpeed
        newcx = cx + self.horizontalSpeed
        if newax < 0:
            newax = 0
            newbx = newax + 40
            newcx = newax + 20
        elif newbx > 800:
            newbx = 800
            newax = newbx - 40
            newcx = newbx - 20
        self.pointA = (newax, ay)
        self.pointB = (newbx, by)
        self.pointC = (newcx, cy)

    
    def goLeft(self, elapsed):
        self.horizontalSpeed += -1 * elapsed
    def goRight(self, elapsed):
        self.horizontalSpeed += 1 * elapsed
    def stop(self):
        self.horizontalSpeed = 0


    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [self.pointA, self.pointB, self.pointC])
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        sx, sy = ship.pointC
        self.rect.x = sx - self.width / 2
        self.rect.y = sy - 10
        self.color = pygame.color.THECOLORS['cyan']
        self.verticalSpeed = -0.1

    def update(self, elapsed):
        self.rect.y += self.verticalSpeed * elapsed
        if self.rect.y < 0:
            self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, self.width, self.height))

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
