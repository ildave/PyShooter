import pygame
import random
import math

class Scene():
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def runScene(self):
        pass

    def handleInput(self):
        pass

class QuitScene(Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        self.font = pygame.font.SysFont('Arial', 40)
        self.byeString = "Bye!"
        w, h = self.font.size(self.byeString)
        sw, sh = self.screen.get_size()
        self.xpos = sw / 2 - w / 2
        self.ypos = sh / 2 - h / 2
        pygame.time.set_timer(pygame.USEREVENT, 2500)

    def runScene(self):
        self.elapsed = self.game.clock.tick(self.game.fps)
        self.screen.fill(pygame.color.THECOLORS['black'])
        textsurface = self.font.render(self.byeString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (self.xpos, self.ypos))
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.done = True
            if event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 0)
                self.game.done = True

class GameOverScene(Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        self.font = pygame.font.SysFont('Arial', 40)
        self.gameOverString = "Game Over!"
        w, h = self.font.size(self.gameOverString)
        sw, sh = self.screen.get_size()
        self.xpos = sw / 2 - w / 2
        self.ypos = sh / 2 - h / 2
        self.smallfont = pygame.font.SysFont('Arial', 20)
        self.subtitleString = "Press SPACE to restart"
        wsmall, hsmall = self.smallfont.size(self.subtitleString)
        self.smallxpos = sw / 2 - wsmall / 2
        self.smallypos = sh / 2 - hsmall / 2 + h

    def runScene(self):
        self.elapsed = self.game.clock.tick(self.game.fps)
        textsurface = self.font.render(self.gameOverString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (self.xpos, self.ypos))
        smalltestsurface = self.smallfont.render(self.subtitleString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(smalltestsurface, (self.smallxpos, self.smallypos))
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitScene = QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_SPACE:
                    gameScene = GameScene(self.screen, self.game)
                    self.game.scene = gameScene


class TitleScene(Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        self.font = pygame.font.SysFont('Arial', 40)
        w, h = self.font.size(self.game.name)
        sw, sh = self.screen.get_size()
        self.titlexpos = sw / 2 - w / 2
        self.titleypos = sh / 2 - h / 2
        self.smallfont = pygame.font.SysFont('Arial', 20)
        self.subtitleString = "Press SPACE to start"
        wsmall, hsmall = self.smallfont.size(self.subtitleString)
        self.smallxpos = sw / 2 - wsmall / 2
        self.smallypos = sh / 2 - hsmall / 2 + h
        self.movementString = "LEFT and RIGHT to move"
        wmovement, hmovement = self.smallfont.size(self.movementString)
        self.movementxpos = sw / 2 - wmovement / 2
        self.movementypos = sh / 2 - hmovement / 2 + h + hsmall
        self.shootString = "SPACE to shoot"
        wshoot, hshoot = self.smallfont.size(self.shootString)
        self.shootxpos = sw / 2 - wshoot / 2
        self.shootypos = sh / 2 - hshoot / 2 + h + hsmall + hmovement
        self.quitString = "Q to quit"
        wquit, hquit = self.smallfont.size(self.quitString)
        self.quitxpos = sw / 2 - wquit / 2
        self.quitypos = sh / 2 - hquit / 2 + h + hsmall + hmovement + hshoot

    def runScene(self):
        self.elapsed = self.game.clock.tick(self.game.fps)
        textsurface = self.font.render(self.game.name, False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (self.titlexpos, self.titleypos))
        smalltestsurface = self.smallfont.render(self.subtitleString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(smalltestsurface, (self.smallxpos, self.smallypos))
        movementsurface = self.smallfont.render(self.movementString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(movementsurface, (self.movementxpos, self.movementypos))
        shootsurface = self.smallfont.render(self.shootString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(shootsurface, (self.shootxpos, self.shootypos))
        quitsurface = self.smallfont.render(self.quitString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(quitsurface, (self.quitxpos, self.quitypos))
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitScene = QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_SPACE:
                    gameScene = GameScene(self.screen, self.game)
                    self.game.scene = gameScene


class GameScene(Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        
        self.resetScreen()

        self.elapsed = 0
        self.ship = Ship(380, 590, 40, 40)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.score = 0
        self.counter = 0
        self.missed = 0

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

        self.stars = self.loadBackground()
    
    def updateBackground(self):
        for s in self.stars:
            y = s.y
            y = y + 1
            x = s.x
            if y > 600:
                y = 0
                x = random.randint(0, 800)
            s.y = y
            s.x = x

    def loadBackground(self):
        stars = []
        for i in range(0, 600, 10):
            for j in range (0, 5):
                x = random.randint(0, 800)
                y = random.randint(i, i + 10)
                s = Star(x, y)
                stars.append(s)
        return stars

    

    def runScene(self):
        self.resetScreen()
        if self.counter % 180 == 0:
            self.spawnEnemy()
        self.elapsed = self.game.clock.tick(self.game.fps)
        self.handleInput()
        self.update()
        self.draw()
        self.checkHits()
        self.counter = self.counter + 1
        if self.missed > 5:
            gameOverScene = GameOverScene(self.screen, self.game)
            self.game.scene = gameOverScene
    
    def resetScreen(self):
        self.screen.fill(pygame.color.THECOLORS['black'])

    def spawnEnemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitScene = QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_LEFT:
                    self.ship.goLeft(self.elapsed)
                if event.key == pygame.K_RIGHT:
                    self.ship.goRight(self.elapsed)
                if event.key == pygame.K_SPACE:
                    self.spawnBullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.ship.stop()
    
    def checkHits(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        self.score += len(hits)

    def update(self):
        self.updateBackground()
        self.ship.update()
        self.enemies.update(self.elapsed, self)
        self.bullets.update(self.elapsed)

    def spawnBullet(self):
        bullet = Bullet(self.ship)
        self.bullets.add(bullet)

    def drawScore(self):
        textsurface = self.font.render('Score: ' + str(self.score), False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (10, 598))

    def drawMissed(self):
        missedString = "Missed: " + str(self.missed)
        w, h = self.font.size(missedString)
        textsurface = self.font.render(missedString, False, pygame.color.THECOLORS['white'])
        x = 800 - w
        self.screen.blit(textsurface, (x, 598))

    def draw(self):
        caption = "FPS: {:.2f}".format(self.game.clock.get_fps())
        pygame.display.set_caption(caption)
        self.drawBackground()
        self.ship.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        self.drawScore()
        self.drawMissed()
        pygame.draw.line(self.screen, pygame.color.THECOLORS['white'], (0, 600), (800, 600))
        pygame.display.flip()

    def drawBackground(self):
        for s in self.stars:
            pygame.draw.rect(self.screen, pygame.color.THECOLORS['white'], (s.x, s.y, 1, 1))


class Game():
    def __init__(self):
        pygame.init()
        self.name = "PyShooter"
        self.screen = pygame.display.set_mode((800, 630))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        pygame.font.init()
        self.scene = TitleScene(self.screen, self)

    def run(self):
        while not self.done:
            self.scene.handleInput()
            self.scene.runScene()
        self.quit()

    def quit(self):
        pygame.quit()


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

        self.pointA = (x, y)
        self.pointB = (x + w, y)
        self.pointC = (x + h/2, y - h)
    
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

        ax, ay = self.pointA
        bx, by = self.pointB
        cx, cy = self.pointC
        newax = ax + self.horizontalSpeed
        newbx = bx + self.horizontalSpeed
        newcx = cx + self.horizontalSpeed
        if newax < 0:
            newax = 0
            newbx = newax + 40
            newcx = newax + 20
        elif newbx > 800:
            newbx = 800
            newax = newbx - 40
            newcx = newbx - 20
        self.pointA = (newax, ay)
        self.pointB = (newbx, by)
        self.pointC = (newcx, cy)

    
    def goLeft(self, elapsed):
        self.horizontalSpeed += -1 * elapsed
    def goRight(self, elapsed):
        self.horizontalSpeed += 1 * elapsed
    def stop(self):
        self.horizontalSpeed = 0


    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [self.pointA, self.pointB, self.pointC])
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        sx, sy = ship.pointC
        self.rect.x = sx - self.width / 2
        self.rect.y = sy - 10
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

    def update(self, elapsed, gameScene):
        self.rect.y += self.verticalSpeed * elapsed
        if self.rect.y > 600:
            self.kill()
            gameScene.missed += 1
        self.rect.x = self.movement()

        if self.rect.x < self.radius:
            self.rect.x = self.radius
        if self.rect.x > 800 - self.radius:
            self.rect.x = 800 - self.radius

    def sinMovement(self):
        return -1 * math.sin(self.rect.y / 50) * self.amplitude + self.startX

    def cosMovement(self):
        return -1 * math.cos(self.rect.y / 50) * self.amplitude + self.startX

class Star():
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    game = Game()
    game.run()
    