import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.radius = random.randint(9, 20)
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.vspeed = random.uniform(0.08, 0.12)
        self.hspeed = random.uniform(0.08, 0.12)
        
        pos = random.randint(0, 3)
        if pos == 0: #up
            self.y = -self.radius * 2
            self.x = random.randint(0, self.game.width - self.radius)
            self.angle = math.pi / 2
        if pos == 1: #down
            self.y = self.game.height + self.radius * 2
            self.x = random.randint(0, self.game.width - self.radius)
            self.angle = -math.pi / 2
        if pos == 2: #left
            self.x = -self.radius * 2
            self.y = random.randint(0, self.game.height - self.radius)
            self.angle = 0
        if pos == 3: #right
            self.x = self.game.width + self.radius * 2
            self.y = random.randint(0, self.game.height - self.radius)
            self.angle = -math.pi

        angleoffset = random.uniform(0, math.pi / 6) - math.pi / 12
        self.angle += angleoffset

        self.rect.x = self.x
        self.rect.y = self.y

        self.color = pygame.color.THECOLORS['red']
        self.active = False
       

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x + self.radius, self.rect.y +  self.radius), self.radius)

    def update(self, elapsed, gameScene):
        self.y +=  math.sin(self.angle) * self.vspeed * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * elapsed
        self.rect.x = self.x
        self.rect.y = self.y
        if not self.active and not self.inGame():
            pass
        if not self.active and self.inGame():
            self.active = True
        if self.active and self.inGame():
            pass
        if self.active and not self.inGame():
            self.kill()


    def inGame(self):
        return (self.x > 0 and self.x < self.game.width) and (self.y > 0 and self.y < self.game.height)
