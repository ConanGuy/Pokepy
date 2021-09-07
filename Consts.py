import ctypes
user32 = ctypes.windll.user32
DEFAULT_SCREEN_SIZE = (user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2)

LEFT = 1
RIGHT = 2
DOWN = 0
UP = 3
ORIENTATION_CODES = {'left': LEFT, 'right': RIGHT, 'down': DOWN, 'up': UP}

import pygame
KEYBINDS = {
    "UP": pygame.K_z,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_q,
    "RIGHT": pygame.K_d
}