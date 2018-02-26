import pygame

class Shield(pygame.sprite.Sprite):
    def __init__(self, game, scene, ship):
        super().__init__()
        self.game = game
        self.scene = scene
        self.ship = ship
        self.ship.shield = True
        self.radius = 35
        self.color = self.ship.color
        self.x = self.ship.x
        self.y = self.ship.y
        timer = self.game.getTimer()
        timer.duration = 15000
        timer.action = self.deactivate

    def deactivate(self):
        self.ship.shield = False
        self.kill()

    def update(self, elapsed):
        self.x = self.ship.x
        self.y = self.ship.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 3)
