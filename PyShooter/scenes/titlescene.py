import pygame
import scenes.scenes
import scenes.quitscene
import scenes.gamescene

class TitleScene(scenes.scenes.Scene):
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
        self.movementString = "LEFT and RIGHT to rotate"
        wmovement, hmovement = self.smallfont.size(self.movementString)
        self.movementxpos = sw / 2 - wmovement / 2
        self.movementypos = sh / 2 - hmovement / 2 + h + hsmall
        self.boostString = "UP to boost"
        wboost, hboost = self.smallfont.size(self.boostString)
        self.boostxpos = sw / 2 - wboost / 2
        self.boostypos = sh / 2 - hboost / 2 + h + hsmall + hmovement
        self.shootString = "SPACE to shoot"
        wshoot, hshoot = self.smallfont.size(self.shootString)
        self.shootxpos = sw / 2 - wshoot / 2
        self.shootypos = sh / 2 - hshoot / 2 + h + hsmall + hmovement + hboost
        self.quitString = "Q to quit"
        wquit, hquit = self.smallfont.size(self.quitString)
        self.quitxpos = sw / 2 - wquit / 2
        self.quitypos = sh / 2 - hquit / 2 + h + hsmall + hmovement + hboost + hshoot 

    def runScene(self):
        self.elapsed = self.game.clock.tick(self.game.fps)
        textsurface = self.font.render(self.game.name, False, pygame.color.THECOLORS['white'])
        self.screen.blit(textsurface, (self.titlexpos, self.titleypos))
        smalltestsurface = self.smallfont.render(self.subtitleString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(smalltestsurface, (self.smallxpos, self.smallypos))
        movementsurface = self.smallfont.render(self.movementString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(movementsurface, (self.movementxpos, self.movementypos))
        boostsurface = self.smallfont.render(self.boostString, False, pygame.color.THECOLORS['white'])
        self.screen.blit(boostsurface, (self.boostxpos, self.boostypos))
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
                    quitScene = scenes.quitscene.QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_SPACE:
                    gameScene = scenes.gamescene.GameScene(self.screen, self.game)
                    self.game.scene = gameScene



