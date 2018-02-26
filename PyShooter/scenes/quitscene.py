import pygame
import scenes.scenes

class QuitScene(scenes.scenes.Scene):
    def __init__(self, screen, game):
        super().__init__(screen, game)
        self.font = pygame.font.SysFont('Arial', 40)
        self.byeString = "Bye!"
        w, h = self.font.size(self.byeString)
        sw, sh = self.screen.get_size()
        self.xpos = sw / 2 - w / 2
        self.ypos = sh / 2 - h / 2
        self.timer = self.game.getTimer()
        self.timer.duration = 2500
        self.timer.action = self.endGame

    def endGame(self):
        self.game.done = True
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
