import pygame
import tripleweapon
import bonus
import math

class TripleWeaponBonus(bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = self.color = pygame.color.THECOLORS['blue']
        self.duration = 150000
        self.size = 20

    def effect(self):
        tw = tripleweapon.TripleWeapon(self.game, self.scene.ship, self.scene)
        self.scene.ship.weapon = tw