import pygame
from Consts import *

class Entity(pygame.sprite.Sprite):

    def __init__(self, id, loc, spritesFile):
        super().__init__()
        self.id = id
        self.loc = loc

        self.dim = (32,48)

        self.sprite_sheet = pygame.image.load(spritesFile)
        self.image = self.get_image(0, self.loc.orientation)
        self.rect = self.image.get_rect()

        self.movingSteps = 0
        self.is_moving = False

    ####################################################

    def update(self):
        self.rect.topleft = self.loc.screenCoords

    def set_image(self, x, y):
        self.image = self.get_image(x, y)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface(self.dim)
        image.blit(self.sprite_sheet, (0,0), (x*self.dim[0], y*self.dim[1], self.dim[0], self.dim[1]))
        image.set_colorkey(image.get_at((0,0)))
        return image

    ####################################################

    def moving(self):

        if self.movingSteps == 0:
            if not self.is_moving:
                self.is_moving = True
                self.movingSteps = 32
            else:
                self.is_moving = False
            return

        if self.movingSteps > 32:
            self.set_image(0, self.loc.orientation)
            self.movingSteps -= 1
            return

        if self.movingSteps > 0:
            lstMovement = [(1,1),(0,-1),(0,1),(1,-1)]
            mvt = lstMovement[self.loc.orientation]
            self.loc.screenCoords[mvt[0]] += mvt[1]

        self.movingSteps -= 1
        self.set_image(int(self.movingSteps/8)%4, self.loc.orientation)

    ####################################################

    def move(self, steps, orientation):
        self.look(orientation)

        lstMovement = [(1,1),(0,-1),(0,1),(1,-1)]
        mvt = lstMovement[orientation]

        newGridCoords = self.loc.gridCoords.copy()
        newGridCoords[mvt[0]] += mvt[1]*steps

        self.movingSteps = steps * (34 if self.movingSteps == None else 32)

    def move_right(self, steps=1):
        self.move(steps, RIGHT)
    def move_left(self, steps=1):
        self.move(steps, LEFT)
    def move_down(self, steps=1):
        self.move(steps, DOWN)
    def move_up(self, steps=1):
        self.move(steps, UP)

    ####################################################

    def look(self, orientation):
        self.loc.orientation = orientation
        self.set_image(0, self.loc.orientation)

    def look_left(self):
        self.look(LEFT)
    def look_right(self):
        self.look(RIGHT)
    def look_up(self):
        self.look(UP)
    def look_down(self):
        self.look(DOWN)

    ####################################################

    def __str__(self):
        return self.id+" "+str(self.loc)