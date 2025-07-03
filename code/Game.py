import pygame

from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill("blue")

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu.run()