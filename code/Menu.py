import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, W_WIDTH, MENU_OPTIONS, C_WHITE, C_BLUE, C_RED, C_GREEN, C_GOLD, C_CYAN
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity('m'))

    def run(self):
        menu_options = 0
        pygame.mixer_music.load('./assets/music.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.fill(C_BLACK)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            self.menu_text(text_size=60, text='AimRushZombie', text_color=C_WHITE, text_center_pos=(300, 50))
            for i in range(len(MENU_OPTIONS)):
                if i == menu_options:
                    self.menu_text(50, MENU_OPTIONS[i], C_BLACK, (W_WIDTH / 2, 140 + 40 * i))
                else:
                    self.menu_text(50, MENU_OPTIONS[i], C_WHITE, (W_WIDTH / 2, 140 + 40 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if(menu_options < len(MENU_OPTIONS) - 1):
                            menu_options += 1
                        else:
                            menu_options = 0
                    if event.key == pygame.K_UP:
                        if menu_options > 0:
                            menu_options -= 1
                        else:
                            menu_options = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_options]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(None, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(text_surf, text_rect)