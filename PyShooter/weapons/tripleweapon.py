import weapons.weapon
import gameobjects.bullet
import math

class TripleWeapon(weapons.weapon.Weapon):

    def shoot(self):
        b1 = gameobjects.bullet.Bullet(self.ship, self.game, 0)
        b2 = gameobjects.bullet.Bullet(self.ship, self.game, math.pi / 6, 10)
        b3 = gameobjects.bullet.Bullet(self.ship, self.game, -math.pi / 6, 10)
        self.scene.bullets.add(b1)
        self.scene.bullets.add(b2)
        self.scene.bullets.add(b3)