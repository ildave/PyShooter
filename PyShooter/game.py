import pygame
import scenes
import timer

class Game():
    def __init__(self):
        pygame.init()
        self.name = "PyShooter"
        self.screen = pygame.display.set_mode((800, 630))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        pygame.font.init()
        self.scene = scenes.TitleScene(self.screen, self)
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