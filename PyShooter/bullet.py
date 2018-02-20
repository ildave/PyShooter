import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.radius = 5
        self.x = int(ship.x + 2 * ship.radius * math.cos(ship.angle))
        self.y = int(ship.y + 2 * ship.radius * math.sin(ship.angle))
        self.angle = ship.angle
        self.angularspeed = -0.001*math.pi

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        self.color = pygame.color.THECOLORS['cyan']
        self.hspeed = 0.15
        self.vspeed = 0.15

    def update(self, elapsed):
        self.y +=  math.sin(self.angle) * self.vspeed * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * elapsed

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        
        if self.x < 0 or self.y < 0 or self.x > 800 or self.y > 600:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
