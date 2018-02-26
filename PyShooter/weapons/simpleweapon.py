import weapons.weapon
import gameobjects.bullet

class SimpleWeapon(weapons.weapon.Weapon):
    def shoot(self):
        b = gameobjects.bullet.Bullet(self.ship, self.game, 0)
        self.scene.bullets.add(b)
