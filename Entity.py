import pygame
from Consts import *

class Entity(pygame.sprite.Sprite):

    def __init__(self, id, loc, spritesFile):
        super().__init__()
        self.id = id
        self.loc = loc
        self.sprite_sheet = pygame.image.load(spritesFile)
        self.image = self.get_image(0, self.loc.orientation)
        self.rect = self.image.get_rect()

    ####################################################

    def update(self):
        self.rect.topleft = self.loc.screenCoords

    def get_image(self, x, y):
        image = pygame.Surface((32,32))
        image.blit(self.sprite_sheet, (0,0), (x*32, y*32, 32, 32))
        image.set_colorkey(image.get_at((0,0)))
        return image

    ####################################################

    def move(self, steps, orientation):
        if self.loc.orientation != orientation:
            self.look(orientation)
        else:
            lstMovement = [(1,1),(0,-1),(0,1),(1,-1)]
            mvt = lstMovement[orientation]
            self.loc.screenCoords[mvt[0]] += mvt[1]

        self.image = self.get_image(0, self.loc.orientation)
        self.rect = self.image.get_rect()

    def move_left(self, steps=1):
        self.move(steps, ORIENTATION_CODES['left'])
    def move_right(self, steps=1):
        self.move(steps, ORIENTATION_CODES['right'])
    def move_up(self, steps=1):
        self.move(steps, ORIENTATION_CODES['up'])
    def move_down(self, steps=1):
        self.move(steps, ORIENTATION_CODES['down'])

    ####################################################

    def look(self, orientation):
        self.loc.orientation = orientation

    def look_left(self):
        self.look(ORIENTATION_CODES['left'])
    def look_right(self):
        self.look(ORIENTATION_CODES['right'])
    def look_up(self):
        self.look(ORIENTATION_CODES['up'])
    def look_down(self):
        self.look(ORIENTATION_CODES['down'])

    ####################################################

    def __str__(self):
        return self.id+" "+str(self.loc)