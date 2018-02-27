import pygame
import math
import gameobjects.bullet

class Helper(pygame.sprite.Sprite):
    def __init__(self, game, scene, ship, direction=1):
        super().__init__()
        self.game = game
        self.scene = scene
        self.ship = ship
        self.radius = 5
        self.direction = direction #1: right, -1:left
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.color = self.ship.color
        self.angle = self.ship.angle
        self.vspeed = self.ship.vspeed
        self.hspeed = self.ship.hspeed
        
        ##calculation for the helper position
        ##on the perpendicular of the line from top and bottom of the ship
        startx, starty = self.ship.originalpoints[1]
        endx, endy = self.ship.originalpoints[3]
        middlex = (endx - startx) / 4
        middley = (endy - starty) / 4
        theta = math.atan2(starty - endy, startx - endx)
        xleft = middlex + (-math.sin(theta) * 50 * self.direction)
        yleft = middley + math.cos(theta) * 50 * self.direction
        self.x = xleft
        self.y = yleft

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

    def update(self, elapsed):
        startx, starty = self.ship.points[1]
        endx, endy = self.ship.points[3]
        middlex = (endx - startx) / 4
        middley = (endy - starty) / 4
        theta = math.atan2(starty - endy, startx - endx)
        xleft = middlex + (-math.sin(theta) * 50 * self.direction)
        yleft = middley + math.cos(theta) * 50 * self.direction
        self.x = xleft
        self.y = yleft
        self.x += self.ship.x
        self.y += self.ship.y

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius


    def draw(self, screen):
        x, y = self.x, self.y
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)
