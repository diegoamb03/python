  
"""Generador de contraseña nivel dificil"""

#generar una contraseña aleatoria en una palabra string
#Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Bienvenido al generador de contraseñas")

num_letras = int(input("cuentas letras? \n")) 
num_simbolos = int(input(f"Cuantos simbolos? \n"))
num_numeros = int(input(f"Cuentos numeros??\n"))

#creamos una lista
password_lista = []

#por cada caracter en rango escoger un caracter aleatorio y sumarlo a la lista
for caracter in range(1, num_letras + 1):
  password_lista.append(random.choice(letras))
  
#por cada caracter en rango escoger un caracter aleatorio y sumarlo a la lista
for caracter in range(1, num_simbolos + 1):
  password_lista += random.choice(simbolos)
  
#por cada caracter en rango escoger un caracter aleatorio y sumarlo a la lista
for caracter in range(1, num_numeros + 1):
  password_lista += random.choice(numeros)

#alteramos la lista para que quede aleatoria
random.shuffle(password_lista)

password = ""
for caracter in password_lista:
  password += caracter

print(f"Tu contraseña es : {password}")
