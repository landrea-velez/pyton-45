# Ejercicio 15: Dadas dos listas de números A y B, indicar si el mayor de la lista A se encuentra en la lista B.

a = []
b = []

n = int(input("Ingresar tamaño de A: "))
for c in range(n):
    x = int(input("Ingresar número: "))
    a.append(x)

m = int(input("Ingresar el tamaño de B: "))
for c in range(m):
    x = int(input("Ingresar número: "))
    b.append(x)

"""mayor_a = -99999
for numero in a:
    if numero > mayor_a:
        mayor_a = numero

bandera = True
for numero in b:
    if numero == mayor_a:
        bandera = True
        break
if bandera:
    print("Si está el mayor de A en B")
else:
    print("NO está el mayor de A en B")
"""

mayor_a = max(a)
if mayor_a in b:
    print("Si está el mayor de A en B")
else:
    print("NO está el mayor de A en B")
