import weapon
import bullet

class SimpleWeapon(weapon.Weapon):
    def shoot(self):
        b = bullet.Bullet(self.ship, self.game, 0)
        self.scene.bullets.add(b)
