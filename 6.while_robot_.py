
#ciclo while  para saltos de robot https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json


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
        
        
#otra forma de hacerlo es while not:
# do this
    
    
