import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship, game):
        super().__init__()
        self.game = game
        self.length = 5
        self.x = int(ship.x + 2 * ship.radius * math.cos(ship.angle))
        self.y = int(ship.y + 2 * ship.radius * math.sin(ship.angle))
        self.angle = ship.angle

        self.image = pygame.Surface([self.length * 2, self.length * 2])
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.length
        self.rect.y = self.y - self.length
        self.color = pygame.color.THECOLORS['cyan']
        self.hspeed = 0.2
        self.vspeed = 0.2

    def update(self, elapsed):
        self.y += math.sin(self.angle) * self.vspeed * elapsed 
        self.x += math.cos(self.angle) * self.hspeed * elapsed

        self.rect.x = self.x - self.length
        self.rect.y = self.y - self.length
        
        if self.x < 0 or self.y < 0 or self.x > self.game.width or self.y > self.game.height:
            self.kill()

    def draw(self, screen):
        px = int(self.x + 2 * self.length * math.cos(self.angle))
        py = int(self.y + 2 * self.length * math.sin(self.angle))
        pygame.draw.line(screen, self.color, (int(self.x), int(self.y)), (int(px), int(py)))
