#programa de entradas de boletas

print("Bienvenido a la entrada de martillo")
altura = int(input("Cual es su altura en cm ?: "))
edad = int(input("Cual es su edad?: "))

#condicionales
if altura > 120:
    print(f"Puede subir al Martillo porque su altura es {altura}")
    if edad >= 18:
        valor_ticket = 12
        print(f"Ticket con valor de {valor_ticket}$ dolares")
    elif edad >= 12:
        valor_ticket = 7
        print(f"Ticket con valor de {valor_ticket}$ dolares")
    else:
        valor_ticket = 5
        print(f"ticket con valor de {valor_ticket}$ dolares")
    quiere_foto = input("Quiere una foto de la atraccion? si/no: ")
    if quiere_foto == "si":
        valor_ticket += 3
        print(f"El valor del ticket es {valor_ticket} $ dolares")
    else:
        print(f"El valor del ticket es {valor_ticket} $ dolares")

else:
    print("Puedes volver cuando seas más grande")
