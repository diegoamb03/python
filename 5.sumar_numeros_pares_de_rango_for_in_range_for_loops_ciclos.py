#Write your code below this row 👇
total = 0
for number in range(0,101,2):
        total += number
        print(number)

print(f"{total}")

#otra forma de matar las pulgas
total_2 = 0
for number in range(1, 101):
        if number % 2 == 0:
                total_2 += number
print(total_2)
