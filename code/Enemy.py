from code.Const import ENTITY_JOGO, W_WIDTH, ENTITY_ENEMY
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_ENEMY[self.name]
        if self.rect.right <= 0:
            self.rect.left = W_WIDTH