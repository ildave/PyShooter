import pygame
import random
import math
import enemies.enemy

class CurvingEnemy(enemies.enemy.Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.angularspeed = -0.0001*math.pi

    def update(self, elapsed, gameScene):
        if random.randint(0, 9) == 0:
            self.angularspeed *= -1
        self.angle += self.angularspeed * elapsed
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

