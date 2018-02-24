import simpleweapon
import tripleweapon
import crossweapon
class Armory():
    def __init__(self, game, ship, scene):
        self.game = game
        self.ship = ship
        self.scene = scene

    def getSimpleWeapon(self):
        return simpleweapon.SimpleWeapon(self.game, self.ship, self.scene)

    def getTripleWeapon(self):
        return tripleweapon.TripleWeapon(self.game, self.ship, self.scene)

    def getCrossWeapon(self):
        return crossweapon.CrossWeapon(self.game, self.ship, self.scene)