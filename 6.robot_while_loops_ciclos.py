def ir_derecha():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    ir_derecha()
    move()
    ir_derecha()
    while front_is_clear():
        move()
    turn_left()
    
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
