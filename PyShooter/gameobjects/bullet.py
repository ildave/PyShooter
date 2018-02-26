import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship, game, degreesOffset, length=5):
        super().__init__()
        self.game = game
        self.length = length
        self.angle = ship.angle + degreesOffset
        self.radius = 3
        
        sx, sy = ship.points[1]
        self.x = sx
        self.y = sy

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.color = pygame.color.THECOLORS['cyan']
        self.hspeed = 0.25
        self.vspeed = 0.25

    def update(self, elapsed): 
        self.x += math.sin(self.angle) * self.vspeed * elapsed 
        self.y += -math.cos(self.angle) * self.hspeed * elapsed

        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.x < 0 or self.y < 0 or self.x > self.game.width or self.y > self.game.height:
            self.kill()


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
