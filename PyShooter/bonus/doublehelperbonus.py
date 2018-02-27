import pygame
import bonus.helperbonus
import gameobjects.texteffect
import gameobjects.helper

class DoubleHelperBonus(bonus.helperbonus.HelperBonus):

    def effect(self):
        h = gameobjects.helper.Helper(self.game, self.scene, self.scene.ship)
        self.scene.effects.add(h)
        h = gameobjects.helper.Helper(self.game, self.scene, self.scene.ship, -1)
        self.scene.effects.add(h)

    def getVisualEffect(self):
        e = gameobjects.texteffect.TextEffect("Double Helper!", self.game)
        return e
