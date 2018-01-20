def turn(direction):
    """turns to the next wall"""
    if direction == "left":
        wall += 1
    elif direction == "right":
        wall -= 1
    else:
        invalid()
    if wall == 1:
        front()
    elif wall == 2:
        left()
    elif wall == 3:
        back()
    elif wall == 4:
        right()
    elif wall == 5:
        wall= 1
        front()
    else:
        wall = 4
        right()



wall = 1


def change(direction):
    """turns to the next wall"""
    if direction == "left":
        return 1
    elif direction == "right":
        return -1
    elif direction == "none"
        return 0
    else:
        invalid()

wall += change(direction)

def wall():
    """prints wall description"""
    if wall == 1:
        front()
    elif wall == 2:
        left()
    elif wall == 3:
        back()
    elif wall == 4:
        right()
    elif wall == 5:
        wall= 1
        front()
    else:
        wall = 4
        right()

def turn(direction):
    """turns to the next wall"""
