import pygame
import random
import math

class Bonus(pygame.sprite.Sprite):
    def __init__(self, game, enemy):
        super().__init__()
        self.game = game
        self.enemy = enemy
        self.size = 10
        self.x = self.enemy.x - self.size / 2
        self.y = self.enemy.y - self.size / 2
        self.image = pygame.Surface([self.size, self.size])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vspeed = random.uniform(0.02, 0.06)
        self.hspeed = random.uniform(0.02, 0.06)
        self.angle = enemy.angle
        angleoffset = random.uniform(0, math.pi / 6) - math.pi / 12
        self.angle += angleoffset

        self.color = pygame.color.THECOLORS['red']

    def update(self, elapsed):
        self.y +=  math.sin(self.angle) * self.vspeed * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * elapsed
        self.rect.x = self.x
        self.rect.y = self.y

        if not self.inGame():
            self.kill()

    def inGame(self):
        return (self.x > 0 and self.x < self.game.width) and (self.y > 0 and self.y < self.game.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 1)
