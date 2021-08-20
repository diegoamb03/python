#suma los digitos del input que escribe el usuario:


two_digit_number = input("Type a two digit number: ")




#Verifique el tipo de datos de two_digit_number
print(type(two_digit_number))

#Obtenga el primer y segundo dígitos usando
#subíndice y luego convierta la cadena en int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Añadir los dos dígitos juntos
two_digit_number = first_digit + second_digit

print(two_digit_number)



"""version en español"""""


# 🚨 Don't change the code below 👇
dos_digitos = input("Escribe 2 numeros ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇


numero_1 = int(dos_digitos[0])
numero_2 = int(dos_digitos[1])
suma_numeros = numero_1 + numero_2
print(suma_numeros)

