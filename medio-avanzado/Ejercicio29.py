# Ejercicio 29: Dada una matriz de NxM elementos, compuesta de 0 y 1 ,
# recorrer cada una de las filas y mostrar el valor decimal equivalente.

""" 
Ejemplo:
(1 1 0 0 0)
(0 1 1 0 1)
(0 0 0 1 1)
"""

n = int(input("Ingresar N: "))
m = int(input("Ingresar M: "))

matriz = []

for fila in range(n):
    matriz.append([])
    for columna in range(m):
        numero = int(input("Ingresar número: "))
        matriz[fila].append(numero)

# Resolución
c = 1
for fila in matriz:
    concatenacion = ""
    for columna in fila:
        concatenacion += str(columna)
    binario_a_decimal = int(concatenacion, 2)
    print(f"Fila {c}: {concatenacion} = {binario_a_decimal}")
    c += 1


# Mostrar matriz
for i in matriz:
    print(*i)
