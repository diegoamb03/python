
#funciones de entradas y multiples entradas.


'''
#Funcion sin entrada
def greet():
        print("Esto es una prueba")
        print("Esto es una prueba")
        print("Esto es una prueba") 

greet()

#Funcion con entrada
def saludo_con_nombres (nombre):
     print(f"hola {nombre}")


nombre = input("Cual es tu nombre? \n")
saludo_con_nombres(nombre)
'''

#ejemplo3
#funcion con multiples entradas

'''
def funcionPrueba(nombre, ubicacion):
        print(f"Hola {nombre} estas en {ubicacion} ?")

nombre = input("Cual es su nombre? \n")
ubicacion = input("Cual es su ubicacion? \n")

funcionPrueba(nombre, ubicacion)

'''

def pruebaMultiplesEntradas (nombre, apellido):
        print(f"hola {nombre}, {apellido} bienvenido al futuro")



pruebaMultiplesEntradas(nombre = "Diego", apellido = "Mendez")
