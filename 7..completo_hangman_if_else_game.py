#Step 3
#se importa el modulo random
import random
lista_palabras = ["boyaca", "armenia", "bucaramanga"]
palabra_escogida = random.choice(lista_palabras)
longitud_palabra = len(palabra_escogida)

#Testing code
print(f'Pssst, the solution is {palabra_escogida}.')

#crea espacios en blanco
display = []
for _ in range(longitud_palabra):
    display += "_"

#TODO-1: -Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
final_de_juego = False

while not final_de_juego:
    adivinar = input("Escoge una letra ").lower()

    #Check guessed letter
    for posicion in range(longitud_palabra):
        letra = palabra_escogida[posicion]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letra == adivinar:
            display[posicion] = letra

    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        final_de_juego = True
        print("Tu ganas.")
