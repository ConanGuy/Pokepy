
import pytmx
import pyscroll
from Consts import *

class Map:

    def __init__(self, _mapFileName):
        dir = "./Maps/map_test_1/"
        self.tmx_data = pytmx.util_pygame.load_pygame(dir+_mapFileName)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, DEFAULT_SCREEN_SIZE)
        self.map_layer.zoom = 3

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)