import pygame

from code.Const import MENU_OPTIONS, W_WIDTH, W_HEIGHT
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
        pygame.display.set_caption("Aim Rush Zombie")

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if(menu_return in [MENU_OPTIONS[0]]):
                level = Level(self.screen, 'bg', menu_return)
                level_return = level.run()
            elif (menu_return in [MENU_OPTIONS[1]]):
                pygame.quit()
                quit()
            else:
                pass
