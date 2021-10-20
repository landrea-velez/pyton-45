# Ejercicio 11: Dada una lista de N números naturales x, mostrar el mayor de ellos.

# Forma lógica
aux = -1
n = int(input("Ingresar N: "))
for c in range(n):
    x = int(input("Ingresar X: "))
    if x > aux:
        aux = x
print("El mayor es:", aux)


lista = []
n = int(input("Ingresar N: "))
for i in range(n):
    x = int(input("Ingresar X: "))
    lista.append(x)
mayor = -1
for numero in lista:
    if numero > mayor:
        mayor = numero
print("El mayor es:", mayor)

# Utilizando max
print("El mayor es:", max(lista))
