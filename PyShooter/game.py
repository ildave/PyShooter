import pygame
import scenes

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

    def run(self):
        while not self.done:
            self.scene.handleInput()
            self.scene.runScene()
        self.quit()

    def quit(self):
        pygame.quit()