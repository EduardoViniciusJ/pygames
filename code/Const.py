# SCREEN
import pygame

W_WIDTH = 576
W_HEIGHT = 324

# MENU OPTONS
MENU_OPTIONS = ["JOGAR" , "SAIR"]

# COLORS
C_BLACK = 0, 0, 0, 255
C_WHITE = 255, 255, 255
C_BLUE = 0, 0, 255
C_RED = 255, 0, 0
C_GREEN = 0, 255, 0
C_YELLOW = 255, 255, 0
C_ORANGE = 255, 165, 0
C_PURPLE = 128, 0, 128
C_PINK = 255, 105, 180
C_GRAY = 128, 128, 128
C_BROWN = 139, 69, 19
C_CYAN = 0, 255, 255
C_NAVY = 0, 0, 128
C_GOLD = 255, 215, 0


# SPEED BACKGROUND
ENTITY_JOGO = {
    'bg0': 0,
    'bg2': 0.5,
    'bg1': 1,
}
# SPEED BACKGROUND
ENTITY_MENU = {
    'm0': 0,
    'm1': 0.5,
    'm2': 0.6,
    'm3': 0.7,
}

# SPEED ENEMY
ENTITY_ENEMY = {
    'z0': 4,
    'z1': 2
}
# SPAWNER ENEMIES
EVENT_ENEMY = pygame.USEREVENT + 10

# HEALTH
ENTITY_HEALTH = {
    'z0': 2,
    'z1': 1,
    'p': 1,
    'bg0': 1000,
    'bg2': 1000,
    'bg1': 1000,
    'm0': 1000,
    'm1': 1000,
    'm2': 1000,
    'm3': 1000,
    'shot': 1,
}

# SPEED SHOT
ENTITY_SHOT = {
    'shot': 10
}

# DEMAGE
ENTITY_DEMAGE = {
    'z0': 1,
    'z1': 1,
    'p': 1,
    'bg0': 0,
    'bg2': 0,
    'bg1': 0,
    'm0': 0,
    'm1': 0,
    'm2': 0,
    'm3': 0,
    'shot': 1,
}