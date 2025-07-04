import pygame
import pygame.math

from code.Const import W_WIDTH, ENTITY_SHOT
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 2
        self.jump_speed = -16
        self.gravity = 0.85
        self.vel_y = 0
        self.is_jumping = False
        self.ground_y = position[1]
        self.shots_fired = 0
        self.last_reload_time = 0
        self.reload_delay = 1000

    def move(self):
        keys = pygame.key.get_pressed()

        # A e D
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Jump W
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

        # Limite para não sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W_WIDTH:
            self.rect.right = W_WIDTH

    def shoot(self, event):
        timer = pygame.time.get_ticks()

        # Se já atirou 15 vezes, precisa esperar recarregar
        if self.shots_fired >= 15:
            if timer - self.last_reload_time >= self.reload_delay:
                self.shots_fired = 0
            else:
                # Ainda recarregando, não atira
                return None

        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            self.shots_fired += 1  #  contador de tiros

            if self.shots_fired == 15:
                self.last_reload_time = timer

            return PlayerShot('shot', position=(self.rect.centerx, self.rect.centery))

        return None
