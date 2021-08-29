
"""CODIGO PARA ENCONTRR EL PUNTAJE MAYOR O MENOR DE UNA LISTA"""


# 🚨 Don't change the code below 👇
puntaje_estudiantes = input("Ingresa una lista de puntajes de estudiantes: ").split()
for n in range(0, len(puntaje_estudiantes)):
  puntaje_estudiantes[n] = int(puntaje_estudiantes[n])
print(puntaje_estudiantes)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

puntuacion_alta = 0
for puntaje in puntaje_estudiantes:
        if puntaje > puntuacion_alta:
                puntuacion_alta = puntaje

print(puntuacion_alta)


#otra forma de realizar esto más sencillo
#min(puntaje_estudiantes)
#max(puntaje_estudiantes)

