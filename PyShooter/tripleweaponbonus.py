import pygame
import tripleweapon
import bonus
import math

class TripleWeaponBonus(bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = self.color = pygame.color.THECOLORS['blue']
        self.duration = 15000
        self.size = 20
        self.originalpoints = [(0, 0), (20, 0), (20, 20), (0, 20)]
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def effect(self):
        tw = tripleweapon.TripleWeapon(self.game, self.scene.ship, self.scene)
        self.scene.ship.weapon = tw
        t = self.game.getTimer()
        t.duration = self.duration
        t.action = self.scene.setSimpleWeapon