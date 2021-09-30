# Ejercicio 15: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

c = 1
while(c <= 10):
    print(f"{c} * 10 = {c*10}")
    c += 1
print("---------")
for c in range(1, 11):
    print(f"{c} * 10 = {c*10}")
