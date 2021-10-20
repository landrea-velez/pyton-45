# Ejercicio 13: Dada una lista de N números enteros x, calcular su promedio. Mostrar el resultado.

n = int(input("Ingresar N: "))
sumador = 0
for c in range(n):
    x = int(input("Ingresar X: "))
    sumador += x
print("El promedio es:", sumador / n)


lista = []
n = int(input("Ingresar N: "))
for c in range(n):
    x = int(input("Ingresar X: "))
    lista.append(x)
sumador = 0
for numero in lista:
    sumador += numero
print("El promedio es:", sumador / len(lista))
