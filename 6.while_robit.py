def giro_derecha():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    giro_derecha()
    move()
    giro_derecha()
    move()
    turn_left()

bandera = True
while bandera == True:  
    jump()
    if at_goal():
        bandera = False
    
