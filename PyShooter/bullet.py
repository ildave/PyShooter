import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship, game, degreesOffset, length=5):
        super().__init__()
        self.game = game
        self.length = length
        self.angle = ship.angle + degreesOffset
        self.bx = int(ship.x + 2 * ship.radius * math.cos(self.angle))
        self.by = int(ship.y + 2 * ship.radius * math.sin(self.angle))
        self.ex = int(self.bx + 2 * self.length * math.cos(self.angle))
        self.ey = int(self.by + 2 * self.length * math.sin(self.angle))
        
        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect()
        self.rect.x = self.ex
        self.rect.y = self.ey
        self.color = pygame.color.THECOLORS['cyan']
        self.hspeed = 0.2
        self.vspeed = 0.2

    def update(self, elapsed):
        self.by += math.sin(self.angle) * self.vspeed * elapsed 
        self.bx += math.cos(self.angle) * self.hspeed * elapsed
        self.ex = int(self.bx + 2 * self.length * math.cos(self.angle))
        self.ey = int(self.by + 2 * self.length * math.sin(self.angle))

        self.rect.x = self.ex
        self.rect.y = self.ey
        
        if self.bx < 0 or self.by < 0 or self.bx > self.game.width or self.by > self.game.height:
            self.kill()

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (int(self.bx), int(self.by)), (int(self.ex), int(self.ey)))
