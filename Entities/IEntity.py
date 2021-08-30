class IEntity:

    def __init__(self, id, loc):
        self.id = id
        self.loc = loc

    def __str__(self):
        return self.id+" "+str(self.loc)