#C
import pygame.constants

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_PURPLE = (163,73,164)
COLOR_DPURPLE = (86,39,87)
COLOR_YELLOW = (241,255,0)
#E
EVENT_ENEMY = pygame.constants.USEREVENT +1
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
}
ENTITY_SPEED = {
'PlayerShot': 1
}

ENTITY_SHOT_DELAY = {
    'Player':50
}

#M
MENU_OPTION = ('NEW GAME SINGLE PLAYER',
               'SCORE',
               'EXIT')
MAX_ENEMIES = 4

#P
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}
#S
SPAWN_TIME = 2000
#w
WIN_WIDTH = 576
WIN_HEIGHT = 320