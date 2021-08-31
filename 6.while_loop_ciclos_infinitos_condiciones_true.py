"""ejemplos de bucle while loop"""

numero_de_veces = 6
while 0 < numero_de_veces:
  numero_de_veces -= 1
  print(numero_de_veces)
  
print("otro ejemplo")
  
i = 1
while i <= 3:
    print(i)
    i += 1
print("2.Programa terminado")


print("otro ejemplo")
i = 1
while i <= 50:
    print(i)
    i = 3 * i + 1
print("Programa terminado")


print("Ejemplo de escribir un numero positivo o negativo")
numero = int(input("Escriba un número positivo: "))

while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")
  
