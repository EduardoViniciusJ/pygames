from abc import ABC, abstractmethod
import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DEMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name  = name
        self.surf = pygame.image.load('./assets/'+ name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DEMAGE[self.name]

    @abstractmethod
    def move(self):
        pass