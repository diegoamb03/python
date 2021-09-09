#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 -Escoger la palabra aleatoria para que se almacene en una variable 
palabra_aleatoria = random.choice(word_list)

#TODO-2 se pregunta al usuario que adivine la palabra

print(f"La palabra_aleatoria es {palabra_aleatoria}")
adivinar = input("Adivina la letra de la palabra: ")


#Traer cada uno de los elementos en la lista
for letra in palabra_aleatoria:
        
        if letra == adivinar:
                print("correcto")
        else:
                print("incorrecto")
                


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
