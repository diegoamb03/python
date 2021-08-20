#calcula el valor de la cuenta por porcentaje y numero de personas



print("Hola, Bienvenido a la calculadora de propina")
#preguntas al usuario
total_cuenta = float(input("Cual es el total de la cuenta?: $"))
porcentaje_escogido = int(input("Cual es el porcentaje de propina que pagaran?: 10, 12 o 15 %" ))
personas = int(input("Cuantas personas pagaran la cuenta?"))

#calculos de division de cuentas
porcentaje_calculado = total_cuenta / 100 * porcentaje_escogido
cuenta_subtotal = porcentaje_calculado + total_cuenta
total_por_persona = cuenta_subtotal / personas
total_por_persona_red = round(total_por_persona, 2)

print(f"Cada persona pagara un total de: {total_por_persona_red}")