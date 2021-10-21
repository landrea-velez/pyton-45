# Ejercicio 14: Dada una lista ordenada de N números x, indicar si hay elementos repetidos.

n = int(input("Ingresar N: "))
lista = []
for c in range(n):
    x = int(input("Ingresar X: "))
    lista.append(x)

# Método de ordenamiento
"""for i in range(0, n-1):
    for j in range(i, n):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux"""
lista.sort()
print(lista)

bandera = False
for numero in lista:
    if lista.count(numero) > 1:
        bandera = True
        break
if bandera:
    print("Existen repetidos")
else:
    print("No existen repetidos")