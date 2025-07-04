from code.Const import ENTITY_MENU, W_WIDTH
from code.Entity import Entity


class BackgroundMenu(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_MENU[self.name]
        if self.rect.right <= 0:
            self.rect.left = W_WIDTH