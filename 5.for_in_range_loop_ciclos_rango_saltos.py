"""Sumar todos los numeros de 1 al 100"""


total = 0
for number in range(1, 101):
        total += number
print(total)

#SUMAR los numeros de 1 a 5050
total_n = 0
for number in range(1, 5050):
        total_n += number

print(total_n)


#sumar los numeros con saltos de 6
total_saltos = 0
for number in range(1, 2000, 3):
        total_saltos += number

print(total_saltos)
