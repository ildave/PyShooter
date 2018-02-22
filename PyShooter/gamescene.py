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
import bonus

class GameScene(scenes.Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        
        self.resetScreen()

        self.elapsed = 0
        self.ship = ship.Ship(20, int(self.game.width / 2), int(self.game.height / 2))
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()

        self.score = 0
        self.energy = 100
        self.boost = 50

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

        self.stars = self.loadBackground()
        
        enemiesTimer = self.game.getRepeateTimer()
        enemiesTimer.duration = 1000
        enemiesTimer.action = self.spawnEnemy

        firstEnemyTimer = self.game.getTimer()
        firstEnemyTimer.duration = 1000
        firstEnemyTimer.action = self.spawnEnemy

        energyTimer = self.game.getRepeateTimer()
        energyTimer.duration = 5000
        energyTimer.action = self.restoreEnergy

        boostTimer = self.game.getRepeateTimer()
        boostTimer.duration = 100
        boostTimer.action = self.restoreBoost

    def restoreBoost(self):
        self.boost += 1
        if self.boost > 50:
            self.boost = 50

    def restoreEnergy(self):
        self.energy += 5
        if self.energy > 100:
            self.energy = 100
    
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
        if self.energy <= 0:
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.stopBoost()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ship.goLeft(self.elapsed)
        if keys[pygame.K_RIGHT]:
            self.ship.goRight(self.elapsed)
        if keys[pygame.K_UP]:
            self.ship.startBoost(self)

    
    def checkHits(self):
        hitEnemies = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        self.score += len(hitEnemies)
        for enemy in hitEnemies:
            expl = sprites.Explosion(enemy.rect.x, enemy.rect.y)
            self.explosions.add(expl)
            t = self.game.getTimer()
            t.duration = 1500
            t.action = expl.kill
            b = bonus.Bonus(self.game, enemy)
            self.bonuses.add(b)
        enemyCollisions = pygame.sprite.spritecollide(self.ship, self.enemies, True)
        for enemy in enemyCollisions:
            self.energy = self.energy - enemy.radius 
            expl = sprites.Explosion(enemy.rect.x, enemy.rect.y)
            self.explosions.add(expl)
            t = self.game.getTimer()
            t.duration = 1500
            t.action = expl.kill
        bonusCollisions = pygame.sprite.spritecollide(self.ship, self.bonuses, True)
        self.score += len(bonusCollisions)
        for b in bonusCollisions:
            expl = sprites.Explosion(b.rect.x, b.rect.y)
            self.explosions.add(expl)
            t = self.game.getTimer()
            t.duration = 500
            t.action = expl.kill

    def update(self):
        self.updateBackground()
        self.ship.update(self.elapsed)
        self.enemies.update(self.elapsed, self)
        self.bullets.update(self.elapsed)
        self.explosions.update(self.elapsed)
        self.bonuses.update(self.elapsed)

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

    def drawStats(self):
        statsString = "Energy: {} Boost: {}".format(self.energy, self.boost)
        w, h = self.font.size(statsString)
        textsurface = self.font.render(statsString, False, pygame.color.THECOLORS['white'])
        x = self.game.width - w
        self.screen.blit(textsurface, (x, self.game.height - 30 - 2))

    def draw(self):
        caption = "FPS: {:.2f}".format(self.game.clock.get_fps())
        pygame.display.set_caption(caption)
        self.drawBackground()
        
        for b in self.bonuses:
            b.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        for e in self.explosions:
            e.draw(self.screen)
        self.ship.draw(self.screen)

        self.drawScore()
        self.drawStats()

        pygame.display.flip()

    def drawBackground(self):
        for s in self.stars:
            pygame.draw.rect(self.screen, pygame.color.THECOLORS['white'], (s.x, s.y, 1, 1))

