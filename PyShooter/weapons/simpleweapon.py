import weapons.weapon
import bullet

class SimpleWeapon(weapons.weapon.Weapon):
    def shoot(self):
        b = bullet.Bullet(self.ship, self.game, 0)
        self.scene.bullets.add(b)
