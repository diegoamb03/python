def giro_completo():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
    turn_left()
def giro_derecha():
    turn_left()
    turn_left()
    turn_left()
for i in range(0,6):
    move()
    giro_completo()
    move()
    giro_derecha()
    move()
    giro_derecha()
    move()
    turn_left()
