from Consts import ORIENTATION_CODES
from Entity import Entity

class Action:

    def __init__(self, name, **kwargs):
        self.name = name

        self.args = {}
        if self.name == "move":
            entity = kwargs.get("entity", None)
            assert isinstance(entity, Entity), "entity type should be Entity, " + str(type(entity).__name__) + " found"
            self.args["entity"] = entity

            orientation = kwargs.get("orientation", None)
            assert orientation in ORIENTATION_CODES.keys(), "orientation should be in " + str(ORIENTATION_CODES.keys()) + ", " + str(orientation) + " found"
            self.args["orientation"] = orientation

            stepsLeft = kwargs.get("steps", None)
            assert stepsLeft > 0 and isinstance(stepsLeft, int), "orientation should be int and equal or more than 0, " + str(stepsLeft) + " found"
            self.args["stepsLeft"] = stepsLeft

