#definicion de While loop  para avanzar con muros al frente

def giro_derecha():
    turn_left()
    turn_left()
    turn_left()
def jump():
    
    turn_left()
    move()
    giro_derecha()
    move()
    giro_derecha()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
