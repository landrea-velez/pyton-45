# Ejercicio 20: Dados 3 dígitos, generar y mostrar el mayor número natural
# que puede escribirse con ellos.

a = int(input("Ingresar A: "))
b = int(input("Ingresar B: "))
c = int(input("Ingresar C: "))

numero = None

if a >= b and b >= c:
    numero = a * 100 + b * 10 + c
elif b >= a and a >= c:
    numero = b * 100 + a * 10 + c
elif c >= a and a >= b:
    numero = c * 100 + a * 10 + b
elif a >= c and c >= b:
    numero = a * 100 + c * 10 + b
elif b >= c and c >= a:
    numero = b * 100 + c * 10 + a
elif c >= b and b >= a:
    numero = c * 100 + b * 10 + a

print("Número generado:", numero)
