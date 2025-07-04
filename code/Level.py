import random
import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from code.Const import C_WHITE, W_WIDTH, W_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, screen, name, game):
        self.screen = screen
        self.name = name
        self.game_mode = game
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg'))
        self.entity_list.append(EntityFactory.get_entity('p'))

        pygame.time.set_timer(EVENT_ENEMY, 500)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(120)
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('z0', 'z1'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        shoot = ent.shoot(event)
                        if shoot is not None:
                            self.entity_list.append(shoot)

            for ent in self.entity_list:
                self.screen.blit(ent.surf, ent.rect)
                ent.move()

            EntityMediator.verify_collision(entity_list=self.entity_list)

            # Verifica se o player morreu
            player_dead = False
            for ent in self.entity_list:
                if isinstance(ent, Player) and ent.health <= 0:
                    player_dead = True
                    break

            EntityMediator.verify_health(entity_list=self.entity_list)

            # Exibir munição
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    ammo_text, ammo_color = ent.get_status_ammo()
                    self.level_text(
                        text_size=25,
                        text=ammo_text,
                        text_color=ammo_color,
                        text_position=(10, W_HEIGHT / 15 + 70)
                    )

            #Informações na tela
            self.level_text(text_size=25, text=f'FPS: {clock.get_fps():.0f}', text_color=C_WHITE, text_position=(10, W_HEIGHT / 22))
            self.level_text(text_size=25, text='PULAR: W', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 10))
            self.level_text(text_size=25, text='DIREITO: D', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 25))
            self.level_text(text_size=25, text='ESQUERDA: A', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 40))
            self.level_text(text_size=25, text='ATIRAR: L', text_color=C_WHITE, text_position=(10, W_HEIGHT / 15 + 55))

            pygame.display.flip()

            #Se o jogador estiver morto envia para tela de game over
            if player_dead:
                self.show_game_over_screen()
                return  # volta ao menu


    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(None, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_position)
        self.screen.blit(text_surf, text_rect)


    #Tela de game over
    def show_game_over_screen(self):
        font = pygame.font.SysFont(None, 50)
        start_time = pygame.time.get_ticks()
        duration = 2000  # 3 segundos

        while True:
            self.screen.fill((0, 0, 0))
            texto = f"Você matou {EntityMediator.killed_enemies} inimigos."
            text_surface = font.render(texto, True, C_WHITE)
            text_rect = text_surface.get_rect(center=(W_WIDTH // 2, W_HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            current_time = pygame.time.get_ticks()
            if current_time - start_time >= duration:
                EntityMediator.killed_enemies = 0  # reset contador para próxima partida
                break
