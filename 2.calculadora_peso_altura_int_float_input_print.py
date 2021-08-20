#Formula es dividir el peso en la altura al cuadrado para saber si es obeso o no




# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_converdida = float(height)
weight_convertida = float(weight)

#calculo BMI

bmi = weight_convertida / (height_converdida**2)
bmi_convertida = int(bmi)
print(bmi_convertida)


"""

##Otra forma de realizarlo más corta


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



#calculo BMI

bmi = float(weight) / float(height)** 2
bmi_convertida = int(bmi)
print(bmi_convertida)


"""