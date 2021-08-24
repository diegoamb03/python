# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Donde Tu quieres poner el tesoro? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#seleccionamos las elecciones de los usuarios por separado
eleccion_numero1 = position[0]
eleccion_numero2 = position[1]
print(eleccion_numero1)
print(eleccion_numero2)

#convertimos esto a numeros

eleccion_int = int(eleccion_numero1)
eleccion_int2 = int(eleccion_numero2)

#row1[eleccion_int] = "x"

if eleccion_int2 == 1 :
        row1[eleccion_int -1] = "x"
elif eleccion_int2 == 2:
        row2[eleccion_int -1] = "x"
else :
        row3[eleccion_int -1] = "x"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
