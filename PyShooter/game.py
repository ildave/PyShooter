import pygame
import scenes.titlescene
import timer

class Game():
    def __init__(self, width, height, fullscreen=True):
        pygame.init()
        self.height = height
        self.width = width
        self.name = "PyShooter"
        if fullscreen:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        pygame.font.init()
        self.scene = scenes.titlescene.TitleScene(self.screen, self)
        self.timers = []

    def getTimer(self):
        t = timer.Timer()
        self.timers.append(t)
        return t

    def getRepeateTimer(self):
        t = timer.RepeateTimer()
        self.timers.append(t)
        return t

    def getRepeatNTimer(self):
        t = timer.RepeateNTimer()
        self.timers.append(t)
        return t

    def run(self):
        while not self.done:
            self.scene.handleInput()
            self.scene.runScene()
            for t in self.timers:
                t.update()
            self.timers = [t for t in self.timers if not t.done]
        self.quit()

    def quit(self):
        pygame.quit()