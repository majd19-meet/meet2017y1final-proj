def up():
    global direction
    new_pos = (fatman.pos()[0], fatman.pos()[1]+SQUARE_SIZE)
    if not (new_pos in wall_pos):
        direction = UP

def down():
    global direction
    new_pos = (fatman.pos()[0], fatman.pos()[1]+SQUARE_SIZE)
    if not (new_pos in wall_pos):
        direction = DOWN

def left():
    global direction
    new_pos = (fatman.pos()[0], fatman.pos()[1]+SQUARE_SIZE)
    if not (new_pos in wall_pos):
        direction = LEFT

def right():
    global direction
    new_pos = (fatman.pos()[0], fatman.pos()[1]+SQUARE_SIZE)
    if not (new_pos in wall_pos):
        direction = RIGHT
