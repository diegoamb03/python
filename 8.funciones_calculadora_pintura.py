#Write your code below this line 👇
'''

importamos el modulo matematico
Al definir la altura el ancho y el cubrimiento
El resultado es = altura * ancho 
El resultado de esta multiplicacion
lo redondeamos a los decimales más cercanos


'''



import math
def paint_calc(height, width, cover):
        result = height * width
        result = math.ceil(result / cover)
        print(f"You'll need {result} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

