from Entities.IEntity import IEntity
from Scripts.Actions.movement import move_left
from Utilities.Localistion import Localisation

e = IEntity('e00001', Localisation("test", [3,0]))
print(e)
move_left(e)
print(e)
move_left(e)
print(e)