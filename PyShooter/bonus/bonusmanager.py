import bonus.bonus
import bonus.tripleweaponbonus
import bonus.crossweaponbonus
import bonus.shieldbonus
import bonus.helperbonus
import bonus.doublehelperbonus
import bonus.healthbonus
import random
import math

class BonusManager():
    def __init__(self, game, scene):
        self.bonuses = ['simple', 'simplemulti', 'tripleweapon', 'crossweapon', 'shield', 'helper', 'health', 'doublehelper']
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
        if bonus == 'helper':
            return self.getHelperBonus()
        if bonus == 'health':
            return self.getHealthBonus()
        if bonus == 'doublehelper':
            return self.getDoubleHelperBonus()

    def getSimpleMultiBonus(self):
        b = self.getSimpleBonusAtLocationAndAngle()
        p = random.randint(2, 10)
        b.value = p
        return b

    def getSimpleBonusAtLocationAndAngle(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.bonus.Bonus(self.game, x, y, angle, self.scene)
        return b

    def getSimpleBonus(self, enemy):
        b = bonus.bonus.Bonus(self.game, enemy.x, enemy.y, enemy.angle, self.scene)
        return b

    def getTripleWeaponBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.tripleweaponbonus.TripleWeaponBonus(self.game, x, y, angle, self.scene)
        return b

    def getCrossWeaponBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.crossweaponbonus.CrossWeaponBonus(self.game, x, y, angle, self.scene)
        return b

    def getShieldBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.shieldbonus.ShieldBonus(self.game, x, y, angle, self.scene)
        return b

    def getHelperBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.helperbonus.HelperBonus(self.game, x, y, angle, self.scene)
        return b

    def getHealthBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.healthbonus.HealthBonus(self.game, x, y, angle, self.scene)
        return b

    def getDoubleHelperBonus(self):
        x = random.randint(100, self.game.width - 100)
        y = random.randint(100, self.game.height - 100)
        angle = random.uniform(0, math.pi)
        b = bonus.doublehelperbonus.DoubleHelperBonus(self.game, x, y, angle, self.scene)
        return b