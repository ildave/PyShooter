import pygame
import bonus
import texteffect
import shield

class ShieldBonus(bonus.bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = self.color = pygame.color.THECOLORS['blue']
        self.duration = 15000
        self.size = 20
        self.originalpoints = [(0, 0), (20, 0), (20, 20), (0, 20)]
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def effect(self):
        s = shield.Shield(self.game, self.scene, self.scene.ship)
        self.scene.effects.add(s)
        
    def getVisualEffect(self):
        e = texteffect.TextEffect("Shield!", self.game)
        return e