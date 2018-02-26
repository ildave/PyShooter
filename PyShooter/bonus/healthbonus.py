import pygame
import random
import bonus.bonus
import gameobjects.texteffect


class HealthBonus(bonus.bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = pygame.color.THECOLORS['blue']
        self.duration = 15000
        self.size = 20
        self.originalpoints = [(0, 0), (20, 0), (20, 20), (0, 20)]
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def effect(self):
        self.scene.energy += random.randint(10, 30)

    def getVisualEffect(self):
        e = gameobjects.texteffect.TextEffect("Health!", self.game)
        return e
