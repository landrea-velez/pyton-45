# Ejercicio 6: Dado un número entero x, mostrar sus N primeras potencias.

x = int(input("Ingresar un número entero: "))
n = int(input("Ingresar N: "))

c = 0
while(c <= n):
    print(f"{x} ** {c} = {x ** c}")
    c += 1

for c in range(n+1):
    print(f"{x} ** {c} = {x ** c}")
