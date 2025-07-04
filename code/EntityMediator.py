from code.Const import W_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:
    killed_enemies  = 0

    @staticmethod
    def verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= W_WIDTH:
                ent.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for  i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)

    #Verifica a colisão entre tiros, zombies e player
    @staticmethod
    def verify_collision_entity(ent1 , ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if  (ent1.rect.right >= ent2.rect.left and
                     ent1.rect.left <= ent2.rect.right and
                     ent1.rect.bottom >= ent2.rect.top and
                     ent1.rect.top <=  ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

    #Verifica e contabiliza cada kill
    @staticmethod
    def verify_health(entity_list: [Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.killed_enemies += 1
                entity_list.remove(ent)


