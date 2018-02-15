import pygame
import random
import math

class Scene():
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        pass

    def handleInput(self):
        pass

class TitleScene(Scene):
    def __init__(self, screen):
        super().__init__(scene)

    def run(self):
        self.font = pygame.font.SysFont('Arial', 40)
        textsurface = self.font.render('PyShooter', False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (10, 598))

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Change scene")



class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 630))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.resetScreen()

        self.elapsed = 0
        self.ship = Ship(390, 550, 40, 40)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.score = 0
        self.counter = 0

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

    def resetScreen(self):
        self.screen.fill(pygame.color.THECOLORS['black'])

    def spawnEnemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)

    def run(self):
        while not self.done:
            self.resetScreen()
            if self.counter % 180 == 0:
                self.spawnEnemy()
            self.elapsed = self.clock.tick(self.fps)
            self.handleInput()
            self.update()
            self.draw()
            self.checkHits()
            self.counter = self.counter + 1

    def checkHits(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        self.score += len(hits)

    def update(self):
        self.ship.update()
        self.enemies.update(self.elapsed)
        self.bullets.update(self.elapsed)

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.goLeft(self.elapsed)
                if event.key == pygame.K_RIGHT:
                    self.ship.goRight(self.elapsed)
                if event.key == pygame.K_SPACE:
                    self.spawnBullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.ship.stop()
    
    def spawnBullet(self):
        bullet = Bullet(self.ship)
        self.bullets.add(bullet)

    def drawScore(self):
        textsurface = self.font.render('Score: ' + str(self.score), False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (10, 598))

    def draw(self):
        caption = "FPS: {:.2f}".format(self.clock.get_fps())
        pygame.display.set_caption(caption)
        self.ship.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        self.drawScore()
        pygame.draw.line(self.screen, pygame.color.THECOLORS['white'], (0, 600), (800, 600))
        pygame.display.flip()

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.width = w
        self.height = h
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = pygame.color.THECOLORS['yellow']
        
        self.horizontalSpeed = 0
    
    def update(self):
        if self.horizontalSpeed > 3:
            self.horizontalSpeed = 3
        if self.horizontalSpeed < -3:
            self.horizontalSpeed = -3
        self.rect.x += self.horizontalSpeed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 800 - self.width:
            self.rect.x = 800 - self.width
    
    def goLeft(self, elapsed):
        self.horizontalSpeed += -1 * elapsed
    def goRight(self, elapsed):
        self.horizontalSpeed += 1 * elapsed
    def stop(self):
        self.horizontalSpeed = 0


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, self.width, self.height))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x + (ship.width / 2) - self.width / 2
        self.rect.y = ship.rect.y
        self.color = pygame.color.THECOLORS['cyan']
        self.verticalSpeed = -0.1

    def update(self, elapsed):
        self.rect.y += self.verticalSpeed * elapsed
        if self.rect.y < 0:
            self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, self.width, self.height))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(9, 20)
        self.image = pygame.Surface([self.radius, self.radius])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.radius)
        self.startX = self.rect.x
        self.rect.y = 0
        self.color = pygame.color.THECOLORS['red']
        self.verticalSpeed = random.uniform(0.095, 0.15)
        self.amplitude = random.randint(80, 120)
        if random.randint(1,2) == 1:
            self.movement = self.sinMovement
        else:
            self.movement = self.cosMovement

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), self.radius)

    def update(self, elapsed):
        self.rect.y += self.verticalSpeed * elapsed
        if self.rect.y > 600:
            self.kill()
        self.rect.x = self.movement()

        if self.rect.x < self.radius:
            self.rect.x = self.radius
        if self.rect.x > 800 - self.radius:
            self.rect.x = 800 - self.radius

    def sinMovement(self):
        return -1 * math.sin(self.rect.y / 50) * self.amplitude + self.startX

    def cosMovement(self):
        return -1 * math.cos(self.rect.y / 50) * self.amplitude + self.startX


game = Game()
game.run()
    
    

