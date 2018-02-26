import pygame
import scenes.scenes
import scenes.quitscene
import scenes.gamescene

class GameOverScene(scenes.scenes.Scene):
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
                    quitScene = scenes.quitscene.QuitScene(self.screen, self.game)
                    self.game.scene = quitScene
                if event.key == pygame.K_SPACE:
                    gameScene = scenes.gamescene.GameScene(self.screen, self.game)
                    self.game.scene = gameScene
