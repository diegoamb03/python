#definicion de diccionarios


diccionario_ejemplo = {
  "key1" : "valor3",
  "key2" : "valor2",
  "key3" : "valor3"
}
print(diccionario_ejemplo)
print("--------------------")

#imprimir una clave del diccionario
print(diccionario_ejemplo["key2"])
print("--------------------")

diccionario_ejemplo2 = {
  "clave1":"valor1",
  "clave2":"valor2",
  "clave3":"valor3"
}

#imprimir una clave del diccionario
print(diccionario_ejemplo2["clave3"])
print("--------------------")

diccionario_ejemplo3 = {
  "paises a visitar" : "Australia, nueva zelanda, Mexico, Panama",
  "lenguajes de programacion a aprender" : "Pyton, JS, m, R" 
}

"""añadiendo nuevos items al diccionario"""
diccionario_vacio ={
  
}

#agregar claves al diccionario

diccionario_vacio["clave_agregada"] = "valor1"
diccionario_vacio["clave_agregada2"] = "valor2"
diccionario_vacio["clave_agregada3"] = "valor3"


#editar una clave agregada o añadir una clave

diccionario_vacio["clave_agregada3"] = "valor modificado"

print(diccionario_vacio)
print("--------------------")

#ciclos trabajados con diccionarios

"""imprimira las claves solamente"""

for thing in diccionario_ejemplo3:
  print(thing)

print("--------------------")


"""imprimira los valores de las claves"""
for key in diccionario_ejemplo3:
  print(key) #imprime la clave
  print(diccionario_ejemplo3[key]) 
  #luego imprime el valor
