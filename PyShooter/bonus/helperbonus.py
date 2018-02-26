import pygame
import bonus.bonus
import gameobjects.texteffect
import gameobjects.helper


class HelperBonus(bonus.bonus.Bonus):
    def __init__(self, game, x, y, angle, scene):
        super().__init__(game, x, y, angle, scene)
        self.color = pygame.color.THECOLORS['blue']
        self.duration = 15000
        self.size = 20
        self.originalpoints = [(0, 0), (20, 0), (20, 20), (0, 20)]
        self.points = self.rotate()
        self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def effect(self):
        h = gameobjects.helper.Helper(self.game, self.scene, self.scene.ship)
        self.scene.effects.add(h)

    def getVisualEffect(self):
        e = gameobjects.texteffect.TextEffect("Helper!", self.game)
        return e