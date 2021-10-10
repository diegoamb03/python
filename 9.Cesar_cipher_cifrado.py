logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""



alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(texto_caesar, cantidad_veces, direccion_veces):
  texto_final = ""
  if direccion_veces == "decodificar":
    cantidad_veces *= -1
  for char in texto_caesar:

    if char in alfabeto:
        posicion = alfabeto.index(char)
        nueva_posicion = posicion + cantidad_veces
        texto_final += alfabeto[nueva_posicion]
    else:
        texto_final += char
    
  print(f"Aqui esta el resultado {direccion_veces} resultado: {texto_final}")

"""
import art
print(art.logo)
"""
print(logo)
continuar_jugando = True
while continuar_jugando == True :
        direccion = input("Escribe 'codificar' para encriptar, Escribe 'decodificar' para desencriptar:\n")
        texto = input("Escribe tu mensaje:\n").lower()
        veces = int(input("Escribe el numero de veces:\n"))
        veces = veces % 26
        caesar(texto_caesar=texto, cantidad_veces=veces, direccion_veces=direccion)
        desicion = input("Quieres comenzar de nuevo el programa 'si' o 'no'? ")

        if desicion == "no":
                continuar_jugando = False
                print("Adios, gracias por jugar")

        
