# Ejercicio 16: Dada una lista de N números x, indicar si la misma viene ordenada ascendentemente.

n = int(input("Ingresar N: "))
lista = []
for c in range(n):
    x = int(input("Ingresar X: "))
    lista.append(x)

bandera = False
for i in range(0, len(lista)-1):
    if lista[i] > lista[i+1]:
        bandera = True
        break

if bandera:
    print("No viene ordenada ascendentemente")
else:
    print("Viene ordenada ascendentemente")
