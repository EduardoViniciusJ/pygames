import pygame
import pygame.math

from code.Const import W_WIDTH
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 2
        self.jump_speed = -16
        self.gravity = 0.85
        self.vel_y = 0
        self.is_jumping = False
        self.ground_y = position[1]

    def move(self):
        keys = pygame.key.get_pressed()

        #AD
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        #Jump
        if keys[pygame.K_w] and not self.is_jumping:
            self.is_jumping = True
            self.vel_y = self.jump_speed
        if self.is_jumping:
            self.rect.y += self.vel_y
            self.vel_y += self.gravity
            if self.rect.y >= self.ground_y:
                self.rect.y = self.ground_y
                self.is_jumping = False
                self.vel_y = 0


    #Impede que o jogador saia da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W_WIDTH:
            self.rect.right = W_WIDTH
