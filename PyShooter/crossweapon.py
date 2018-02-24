import weapon
import bullet
import math

class CrossWeapon(weapon.Weapon):
    def shoot(self):
        b1 = bullet.Bullet(self.ship, self.game, 0)
        b2 = bullet.Bullet(self.ship, self.game, math.pi / 2, 10)
        b3 = bullet.Bullet(self.ship, self.game, math.pi, 10)
        b4 = bullet.Bullet(self.ship, self.game, 3 * math.pi / 2, 10)
        self.scene.bullets.add(b1)
        self.scene.bullets.add(b2)
        self.scene.bullets.add(b3)
        self.scene.bullets.add(b4)