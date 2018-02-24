import simpleweapon
import tripleweapon
import crossweapon
import random

class Armory():
    def __init__(self, game, ship, scene):
        self.weapons = ['simple', 'triple', 'cross']
        self.game = game
        self.ship = ship
        self.scene = scene

    def getRandomWeapon(self):
        weapon = random.choice(self.weapons)
        if weapon == 'simple':
            return self.getSimpleWeapon()
        if weapon == 'triple':
            return self.getTripleWeapon()
        if weapon == 'cross':
            return self.getCrossWeapon()

    def getSimpleWeapon(self):
        return simpleweapon.SimpleWeapon(self.game, self.ship, self.scene)

    def getTripleWeapon(self):
        return tripleweapon.TripleWeapon(self.game, self.ship, self.scene)

    def getCrossWeapon(self):
        return crossweapon.CrossWeapon(self.game, self.ship, self.scene)