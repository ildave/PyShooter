import pygame

class TextEffect(pygame.sprite.Sprite):
    def __init__(self, text, game):
        super().__init__()
        self.text = text
        self.game = game
        self.fontsize = 150
        self.font = pygame.font.SysFont('Arial', self.fontsize)
        self.w, self.h = self.font.size(self.text)
        self.xpos = self.game.width / 2 - self.w / 2
        self.ypos = self.game.height / 2 - self.h / 2
        self.alpha = 128

    def update(self, elapsed):
        self.fontsize += 4
        if self.fontsize > 200:
            self.alpha -= 4
        self.font = pygame.font.SysFont('Arial', self.fontsize)
        self.w, self.h = self.font.size(self.text)
        self.xpos = self.game.width / 2 - self.w / 2
        self.ypos = self.game.height / 2 - self.h / 2

        if self.alpha <= 0:
            self.kill()
        

    def draw(self, screen):
        textsurface = self.font.render(self.text, False, pygame.color.THECOLORS['white'])
        textsurface.set_alpha(self.alpha)
        screen.blit(textsurface, (self.xpos, self.ypos))
