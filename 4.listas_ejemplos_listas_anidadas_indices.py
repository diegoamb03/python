fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

fruits[-1] = "Melons"
fruits.append("Lemons")
#print(fruits)


#ejemplos de listas anidadas.

fruits_2  = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]

#como manejar los indices de las listas anidadas
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3]) 
print(dirty_dozen[1][1])

#ejemplo de listas anidadas

instrumentos = ["Piano", "Flauta", "Violin", "contrabajo", "Guitarra"]

lugares = ["Venecia", "universidad nacional"]

musica = [instrumentos, lugares]
print(musica)
print(musica[1][1])
