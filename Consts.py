import ctypes
user32 = ctypes.windll.user32
DEFAULT_SCREEN_SIZE = (user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2)

ORIENTATION_CODES = {'left': 1, 'right': 2, 'down': 0, 'up':3}

import pygame
KEYBINDS = {
    "UP": pygame.K_z,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_q,
    "RIGHT": pygame.K_d
}