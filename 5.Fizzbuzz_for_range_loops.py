#Write your code below this row 👇
"""Juego de niños de Fizz Buzz Si es divisible en 3 fiz si es 5 Buzz y si es ambos Fiz Bus"""

for number in range(1,100):
        if number % 3 == 0 and number % 5 ==0:
                print("FizzBuzz")
        elif number % 3 == 0:
                print("Fizz")
        elif number % 5 ==0:
                print("Buzz")

        else:
                print(number)
