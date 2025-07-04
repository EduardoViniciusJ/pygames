from code.Background import Background
from code.BackgroundMenu import BackgroundMenu
from code.Const import W_WIDTH, W_HEIGHT
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for layer in ['bg0', 'bg1', 'bg2']:
                    list_bg.append(Background(layer, (0, 0)))
                    list_bg.append(Background(layer, (W_WIDTH, 0)))
                return list_bg
            case 'm':
                list_m = []
                for layer in ['m0', 'm1', 'm2', 'm3']:
                    list_m.append(BackgroundMenu(layer, (0, 0)))
                    list_m.append(BackgroundMenu(layer, (W_WIDTH, 0)))
                return list_m
            case 'p':
                return Player('p', (10, W_HEIGHT / 2 + 90))
            case 'z0':
                return Enemy('z0', (W_WIDTH + 10, W_HEIGHT / 2 + 100))
            case 'z1':
                return Enemy('z1', (W_WIDTH + 10, W_HEIGHT / 2 + 100))