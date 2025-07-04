import random
from tkinter.constants import SEL_FIRST

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from code.Const import C_WHITE, W_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, game):
        self.screen = screen
        self.name = name
        self.game_mode = game
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg'))
        self.entity_list.append(EntityFactory.get_entity('p'))

        pygame.time.set_timer(EVENT_ENEMY, 4000)


    def run(self):
        clock= pygame.time.Clock()
        while True:
            clock.tick(120)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('z0', 'z1'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            self.level_text(text_size=25, text=f'FPS: {clock.get_fps() :.0f}', text_color=C_WHITE, text_position=(10, W_HEIGHT / 22))
            self.level_text(text_size=25, text='PULAR: W', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 10))
            self.level_text(text_size=25, text='DIREITO: D', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 25))
            self.level_text(text_size=25, text='ESQUERDA: A', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 40))
            self.level_text(text_size=25, text='ATIRAR: L', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 55))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(None, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_position)
        self.screen.blit(text_surf, text_rect)
