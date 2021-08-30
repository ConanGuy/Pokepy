def move_left(entity, steps=1):
    if entity.loc.orientation != 3:
        entity.loc.orientation = 3
    else:
        entity.loc.coords[0] -= 1

def move_right(entity, steps=1):
    if entity.loc.orientation != 1:
        entity.loc.orientation = 1
    else:
        entity.loc.coords[0] += 1

def move_up(entity, steps=1):
    if entity.loc.orientation != 0:
        entity.loc.orientation = 0
    else:
        entity.loc.coords[1] -= 1

def move_down(entity, steps=1):
    if entity.loc.orientation != 2:
        entity.loc.orientation = 2
    else:
        entity.loc.coords[1] += 1

####################################################

def look_left(entity):
    entity.loc.orientation = 3

def look_right(entity):
    entity.loc.orientation = 1

def look_up(entity):
    entity.loc.orientation = 0

def look_down(entity):
    entity.loc.orientation = 2

