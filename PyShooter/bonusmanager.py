import bonus
import tripleweaponbonus
import crossweaponbonus
import shieldbonus
import random
import math

class BonusManager():
    def __init__(self, game, scene):
        self.bonuses = ['simple', 'simplemulti', 'tripleweapon', 'crossweapon', 'shield']
        self.game = game
        self.scene = scene

    def getRandomBonus(self):
        bonus = random.choice(self.bonuses)
        if bonus == 'simple':
            return self.getSimpleBonusAtLocationAndAngle()
        if bonus == 'simplemulti':
            return self.getSimpleMultiBonus()
        if bonus == 'tripleweapon':
            return self.getTripleWeaponBonus()
        if bonus == 'crossweapopn':
            return self.getCrossWeaponBonus()
        if bonus == 'shield':
            return self.getShieldBonus()

    def getSimpleMultiBonus(self):
        b = self.getSimpleBonusAtLocationAndAngle()
        p = random.randint(2, 10)
        b.value = p
        return b

    def getSimpleBonusAtLocationAndAngle(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.Bonus(self.game, x, y, angle, self.scene)
        return b

    def getSimpleBonus(self, enemy):
        b = bonus.Bonus(self.game, enemy.x, enemy.y, enemy.angle, self.scene)
        return b

    def getTripleWeaponBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = tripleweaponbonus.TripleWeaponBonus(self.game, x, y, angle, self.scene)
        return b

    def getCrossWeaponBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = crossweaponbonus.CrossWeaponBonus(self.game, x, y, angle, self.scene)
        return b

    def getShieldBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = shieldbonus.ShieldBonus(self.game, x, y, angle, self.scene)
        return b

