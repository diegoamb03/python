
"""CODIGO PARA ENCONTRR EL PUNTAJE MAYOR O MENOR DE UNA LISTA"""


# ๐จ Don't change the code below ๐
puntaje_estudiantes = input("Ingresa una lista de puntajes de estudiantes: ").split()
for n in range(0, len(puntaje_estudiantes)):
  puntaje_estudiantes[n] = int(puntaje_estudiantes[n])
print(puntaje_estudiantes)
# ๐จ Don't change the code above ๐

#Write your code below this row ๐

puntuacion_alta = 0
for puntaje in puntaje_estudiantes:
        if puntaje > puntuacion_alta:
                puntuacion_alta = puntaje

print(puntuacion_alta)


#otra forma de realizar esto mรกs sencillo
#min(puntaje_estudiantes)
#max(puntaje_estudiantes)

