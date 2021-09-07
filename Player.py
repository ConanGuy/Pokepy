from Entity import Entity
from Utilities.Localisation import Localisation

class Player(Entity):

    def __init__(self, _coords=[0,0], _orientation=0):
        super().__init__("player", Localisation(None,_coords, _orientation), "Sprites/Boy/boy.bmp")