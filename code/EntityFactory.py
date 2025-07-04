from code.Background import Background
from code.BackgroundMenu import BackgroundMenu
from code.Const import W_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for layer in ['bg0', 'bg1', 'bg2']:
                    list_bg.append(Background(layer, (0,0)))
                    list_bg.append(Background(layer, (W_WIDTH,0)))
                return list_bg
            case 'm':
                list_m = []
                for layer in ['m0', 'm1', 'm2', 'm3']:
                    list_m.append(BackgroundMenu(layer, (0, 0)))
                    list_m.append(BackgroundMenu(layer, (W_WIDTH, 0)))
                return list_m