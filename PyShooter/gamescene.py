import pygame
import scenes
import quitscene
import gameoverscene
import sprites
import ship
import random
import enemy
import bullet
import math

class GameScene(scenes.Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        
        self.resetScreen()

        self.elapsed = 0
        self.ship = ship.Ship(20, int(self.game.width / 2), int(self.game.height / 2))
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        self.score = 0
        self.missed = 0

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

        self.stars = self.loadBackground()
        
        enemiesTimer = self.game.getRepeateTimer()
        enemiesTimer.duration = 3000
        enemiesTimer.action = self.spawnEnemy

        firstEnemyTimer = self.game.getTimer()
        firstEnemyTimer.duration = 1000
        firstEnemyTimer.action = self.spawnEnemy
    
    def updateBackground(self):
        for s in self.stars:
            y = s.y
            y = y + 1
            x = s.x
            if y > self.game.height:
                y = 0
                x = random.randint(0, self.game.width)
            s.y = y
            s.x = x

    def loadBackground(self):
        stars = []
        for i in range(0, self.game.height, 10):
            for j in range (0, 5):
                x = random.randint(0, self.game.width)
                y = random.randint(i, i + 10)
                s = sprites.Star(x, y)
                stars.append(s)
        return stars

    def runScene(self):
        self.resetScreen()
        self.elapsed = self.game.clock.tick(self.game.fps)
        self.handleInput()
        self.update()
        self.draw()
        self.checkHits()
        if self.missed > 5:
            gameOverScene = gameoverscene.GameOverScene(self.screen, self.game)
            self.game.scene = gameOverScene
    
    def resetScreen(self):
        self.screen.fill(pygame.color.THECOLORS['black'])

    def spawnEnemy(self):
        e = enemy.Enemy(self.game)
        self.enemies.add(e)

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitScene = quitscene.QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_SPACE:
                    self.spawnBullet()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ship.goLeft(self.elapsed)
        if keys[pygame.K_RIGHT]:
            self.ship.goRight(self.elapsed)

    
    def checkHits(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        self.score += len(hits)
        for enemy in hits:
            expl = sprites.Explosion(enemy)
            self.explosions.add(expl)
            t = self.game.getTimer()
            t.duration = 1500
            t.action = expl.kill

    def update(self):
        self.updateBackground()
        self.ship.update(self.elapsed)
        self.enemies.update(self.elapsed, self)
        self.bullets.update(self.elapsed)
        self.explosions.update(self.elapsed)

    def spawnBullet(self):
        b = bullet.Bullet(self.ship, self.game, 0)
        self.bullets.add(b)
        b = bullet.Bullet(self.ship, self.game, math.pi / 6, 10)
        self.bullets.add(b)
        b = bullet.Bullet(self.ship, self.game, -math.pi / 6, 10)
        self.bullets.add(b)

    def drawScore(self):
        textsurface = self.font.render('Score: ' + str(self.score), False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (10, self.game.height - 30 - 2))

    def drawMissed(self):
        missedString = "Missed: " + str(self.missed)
        w, h = self.font.size(missedString)
        textsurface = self.font.render(missedString, False, pygame.color.THECOLORS['white'])
        x = self.game.width - w
        self.screen.blit(textsurface, (x, self.game.height - 30 - 2))

    def draw(self):
        caption = "FPS: {:.2f}".format(self.game.clock.get_fps())
        pygame.display.set_caption(caption)
        self.drawBackground()
        self.ship.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        for e in self.explosions:
            e.draw(self.screen)
        self.drawScore()
        self.drawMissed()
        pygame.draw.line(self.screen, pygame.color.THECOLORS['white'], (0, self.game.height - 30), (self.game.width, self.game.height - 30))
        pygame.display.flip()

    def drawBackground(self):
        for s in self.stars:
            pygame.draw.rect(self.screen, pygame.color.THECOLORS['white'], (s.x, s.y, 1, 1))

