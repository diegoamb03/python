#Formula es dividir el peso en la altura al cuadrado para saber si es obeso o no




# ๐จ Don't change the code below ๐
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
height_converdida = float(height)
weight_convertida = float(weight)

#calculo BMI

bmi = weight_convertida / (height_converdida**2)
bmi_convertida = int(bmi)
print(bmi_convertida)


"""

##Otra forma de realizarlo mรกs corta


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



#calculo BMI

bmi = float(weight) / float(height)** 2
bmi_convertida = int(bmi)
print(bmi_convertida)


"""