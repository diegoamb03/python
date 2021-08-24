# Split string method
names_string = input("Dame todos los nombres, separados por comas. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names_string)
print(names)

#Importamos  modulo aleatorio
import random
#almacenamos longuitud de la lista en una variable
longuitud = len(names)
#almacenamos un numero aleatorio teniendo en cuenta la longuitud inicuial y final de la lista inicia en 0 y termina con la longitud
indice_aleatorio = random.randrange(0, longuitud)
#almacenamos en la variable la eleccion aleatoria
usuario = names[indice_aleatorio]
print(usuario)

print(f"El usuario {usuario}, pagara la cuenta")
