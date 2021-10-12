# Teoria: tuplas

# Definir una tupla
tupla = (1, 2, 3, 4)

print(tupla)
print("Primer elemento:", tupla[0])

# Modificar el valor
print("Tupla sin modificar:", tupla)
aux_lista = list(tupla)
aux_lista[0] = 999
tupla = tuple(aux_lista)
print("Tupla modificada:", tupla)

# Eliminar
tamanio_tupla = len(tupla)
print("El tamanio de la tupla es:", tamanio_tupla)

# Concatenar tuplas
tupla_nueva = (1, 2, 3) + (4, 5, 6)
print("Nueva tupla:", tupla_nueva)
