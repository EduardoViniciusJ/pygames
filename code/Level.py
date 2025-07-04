import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, game):
        self.screen = screen
        self.name = name
        self.game_mode = game
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()