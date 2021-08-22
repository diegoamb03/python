# 🚨 Don't change the code below 👇
print("Bienvenido a la calculadora de amor!")
nombre1 = input("cual es su nombre? \n")
nombre2 = input("cual es el nombre del candidato? \n")
# 🚨 Don't change the code above 👆


nombre_min = nombre1.lower() + nombre2.lower()


#contamos cuantas veces esta en True
veces_true = 0
veces_t = nombre_min.count("t")
veces_true += veces_t
veces_r = nombre_min.count("r")
veces_true += veces_r
veces_u = nombre_min.count("u")
veces_true += veces_u
veces_e = nombre_min.count("e")
veces_true += veces_e
print(veces_true)

#veces love
veces_love = 0
veces_l = nombre_min.count("l")
veces_love += veces_l
veces_o = nombre_min.count("o")
veces_love += veces_o
veces_v = nombre_min.count("v")
veces_love += veces_v
veces_e = nombre_min.count("e")
veces_love += veces_e
print(veces_love)


veces_true_convertido = str(veces_true)
veces_love_convertido = str(veces_love)
convinacion_true_love = veces_true_convertido + veces_love_convertido
print(convinacion_true_love)
convinacion_true_love_int = int(convinacion_true_love)

#condicionales
if convinacion_true_love_int < 10 or convinacion_true_love_int > 90 :
        print(f"Tu puntaje es {convinacion_true_love_int}, van juntos como coca y mentos.")
elif convinacion_true_love_int >= 40 and convinacion_true_love_int <= 50:
        print(f"Tu puntaje es {convinacion_true_love_int}, Estan bien juntos")
else :
        print(f"Tu puntaje es {convinacion_true_love_int}")



"""
#otra forma de realizar

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  """
