import pygame
import math
import gameobjects.bullet

class Helper(pygame.sprite.Sprite):
    def __init__(self, game, scene, ship):
        super().__init__()
        self.game = game
        self.scene = scene
        self.ship = ship
        self.radius = 5
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.color = self.ship.color
        self.angle = self.ship.angle
        self.vspeed = self.ship.vspeed
        self.hspeed = self.ship.hspeed
        self.x = self.ship.x - 50
        self.y = self.ship.y
        self.originalpoints = [(0, 0)]
        self.points = self.originalpoints
        self.rotate()
        self.translate()
        
        deathTimer = self.game.getTimer()
        deathTimer.duration = 30000
        deathTimer.action = self.remove

        self.shootTimer = self.game.getRepeateTimer()
        self.shootTimer.duration = 500
        self.shootTimer.action = self.shoot

    def shoot(self):
        b = gameobjects.bullet.Bullet(self.ship, self.game, 0)
        b.x = self.x
        b.y = self.y
        b.rect.x = b.x
        b.rect.y = b.y
        self.scene.bullets.add(b)

    def remove(self):
        self.shootTimer.cancel()
        self.kill()

    def translate(self):
       self.points = [(a + self.x, b + self.y) for a, b in self.points]

    def rotate(self):
        newPoints = []
        for x, y in self.originalpoints:
            newx = x * math.cos(self.angle) - y * math.sin(self.angle)
            newy = x * math.sin(self.angle) + y * math.cos(self.angle)
            newPoints.append((newx, newy))

        self.points = newPoints

    def update(self, elapsed):
        self.angle = self.ship.angle
        self.x += math.sin(self.angle) * self.vspeed * self.ship.boost * elapsed 
        self.y += -math.cos(self.angle) * self.hspeed * self.ship.boost * elapsed

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        self.points = self.originalpoints
        self.rotate()
        self.translate()


    def draw(self, screen):
        x, y = self.points[0]
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)
