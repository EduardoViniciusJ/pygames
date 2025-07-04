from code.Const import W_WIDTH, ENTITY_MENU, ENTITY_JOGO
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_JOGO[self.name]
        if self.rect.right <= 0:
            self.rect.left = W_WIDTH