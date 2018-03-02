import pygame
import random
import math
import enemies.enemy

class ZigZagEnemy(enemies.enemy.Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.timer = self.game.getRepeateTimer()
        self.timer.duration = 3000
        self.timer.action = self.changeAngle

    def changeAngle(self):
        if random.randint(0, 1) == 0:
            self.angle += math.pi / 2
        else:
            self.angle -= math.pi / 2

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
            self.timer.cancel()


