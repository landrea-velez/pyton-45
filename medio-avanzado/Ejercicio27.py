# Ejercicio 27
"""
Dada una matriz de NxM elementos, calcular el promedio de cada fila y de
cada columna. Mostrar en pantalla la matriz cargada y los promedios correspondientes.
"""

n = int(input("Ingresar N: "))
m = int(input("Ingresar M: "))

# Cargar matriz
matriz = []

for fila in range(n):
    matriz.append([])
    for columna in range(m):
        numero = int(input("Ingresar número: "))
        matriz[fila].append(numero)

# Promedio de filas
c = 1
for fila in matriz:
    sumador = sum(fila)
    promedio = sumador // m
    print(f"Promedio de la fila {c}:", promedio)
    c += 1

# Promedio de las columnas
for columna in range(m):
    sumador = 0
    for fila in matriz:
        sumador += fila[columna]
    promedio = sumador // n
    print(f"Promedio de la columna {columna+1}:", promedio)

# Mostrar matriz
for i in matriz:
    print(*i)
