# Ejercicio 28: Dada una matriz de caracteres, ordenar cada columna alfabéticamente.

n = int(input("Ingresar N: "))
m = int(input("Ingresar M: "))

# Cargar matriz
matriz = []
for fila in range(n):
    matriz.append([])
    for columna in range(m):
        caracter = input("Ingresar caracter: ")
        matriz[fila].append(caracter)

# Mostrar matriz
print("--- Matriz original ---")
for i in matriz:
    print(*i)

# Algoritmo
for columna in range(n):
    fila_aux = []
    for fila in matriz:
        fila_aux.append(fila[columna])
    fila_aux = sorted(fila_aux)
    f = 0
    for fila in matriz:
        fila[columna] = fila_aux[f]
        f += 1

# Matriz nueva
print("--- Matriz nueva ---")
for i in matriz:
    print(*i)
