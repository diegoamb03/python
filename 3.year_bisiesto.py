# 🚨 Don't change the code below 👇
year = int(input("Cual año quieres comprobar si es biciesto? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



#comprobar que un año sea biciesto
print(year)
if year %  4 == 0 :
        
        if year % 100 == 0:
                if year % 400 == 0:
                        print("Es un año biciesto")
                else:
                        print("No es un año biciesto")
        else:
                print("Es un año biciesto")
        
else:
        print("No es un año biciesto")
