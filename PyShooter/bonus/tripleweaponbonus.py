import pygame
import bonus.bonus
import gameobjects.texteffect

class TripleWeaponBonus(bonus.bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = self.color = pygame.color.THECOLORS['blue']
        self.duration = 15000
        self.size = 20
        self.originalpoints = [(0, 0), (20, 0), (20, 20), (0, 20)]
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def effect(self):
        tw = self.scene.weaponarmory.getTripleWeapon()
        self.scene.ship.weapon = tw
        t = self.game.getTimer()
        t.duration = self.duration
        t.action = self.scene.setSimpleWeapon

    def getVisualEffect(self):
        e = gameobjects.texteffect.TextEffect("Triple shoot!", self.game)
        return e