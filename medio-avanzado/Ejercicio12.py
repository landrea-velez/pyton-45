# Ejercicio 12: Dada una lista de N números naturales x, mostrar el menor de ellos.

n = int(input("Ingresar N: "))
lista = []
for c in range(n):
    x = int(input("Ingresar X: "))
    lista.append(x)
print("El menor es:", min(lista))
