class Localisation:

    def __init__(self, _map, _coords, _orientation=0):
        assert isinstance(_map, str) or _map == None, "_map should be str, "+str(type(_map).__name__)+" detected"
        assert isinstance(_coords, list), "_coords should be list, "+str(type(_coords).__name__)+" detected"
        assert isinstance(_orientation, int), "_coords should be int, "+str(type(_orientation).__name__)+" detected"
        assert len(_coords) == 2, "_coords len should be 2, "+str(len(_coords))+" detected" 
        assert 0 <= _orientation <= 3, "_orientation len should be between 0 and 3 included, "+_orientation+" detected" 

        self.map = _map
        self.gridCoords = _coords
        self.screenCoords = list(map(lambda x: x*32, _coords))
        self.orientation = _orientation

    def __str__(self):
        return self.map + " " + str(self.coords) + " " + str(self.orientation)

if __name__ == '__main__':
    print(Localisation("map", [1,2]))