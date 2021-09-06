from Entity import Entity
from Utilities.Localisation import Localisation
import pytmx
import pygame
import pyscroll
from Consts import *
from Map import Map
from Player import Player

class Game:

    def __init__(self):
        self.win = pygame.display.set_mode((0,0), pygame.NOFRAME)
        self.map = Map("map_test_1.tmx")
        self.player = Player([4,4])

        self.map.group.add(self.player)

        self.pressed_keys = []

        self.actionsToRunEveryFrame = []

        self.run()

    def run(self):

        clock = pygame.time.Clock()
        running = True
        while running:

            dt = clock.tick(60)

            keys = pygame.key.get_pressed()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit(0)
            
                if e.type == pygame.KEYDOWN:
                    self.pressed_keys.append(e.key)
                if e.type == pygame.KEYUP:
                    self.pressed_keys.remove(e.key)

            self.run_key_event()

            self.map.group.update()
            self.map.group.draw(self.win)
            pygame.display.update()

    def run_key_event(self):
        if len(self.pressed_keys) == 0:
            return

        current_key = self.pressed_keys[-1]
        if current_key == KEYBINDS["UP"]:
            self.player.move_up()
        if current_key == KEYBINDS["DOWN"]:
            self.player.move_down()
        if current_key == KEYBINDS["LEFT"]:
            self.player.move_left()
        if current_key == KEYBINDS["RIGHT"]:
            self.player.move_right()