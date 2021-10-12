# Teoria: listas y matrices

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Mostrar matriz
for fila in matriz:
    print(*fila)

# Cantidad de filas
tamanio_filas = len(matriz)

# Cantidad de columnas
tamanio_columnas = len(matriz[0])
print("Cantidad de filas:", tamanio_filas)
print("Cantidad de columnas:", tamanio_columnas)

# Mostrar fila
print("Fila 1:", matriz[0])
print("Fila 2 - Columna 2:", matriz[1][1])
