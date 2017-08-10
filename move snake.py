import turtle
def move_fatman():
    if direction==RIGHT:
        new_pos=(x_pos+SQUARE_SIZE,y.pos)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==LEFT:
        new_pos=(x_pos-SQUARE_SIZE,y.pos)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==UP:
        new_pos=(x_pos,y.pos+SQUARE_SIZE)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==DOWN:
        new_pos=(x_pos,y.pos-SQUARE_SIZE)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)
