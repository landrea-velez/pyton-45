# Teoria - Diccionarios

# Definir un diccionario

diccionario = {"rojo": "red", "azul": "blue", "amarillo": "yellow"}

# Mostramos
print("El color rojo en inglés es:", diccionario["rojo"])
print("El color azul en inglés es:", diccionario["azul"])
print("El color amarillo en inglés es:", diccionario["amarillo"])

# Agregar
diccionario["verde"] = "grin"
diccionario.update({"blanco": "white"})
print(diccionario)

# Modificar
diccionario["verde"] = "green"
diccionario.update({"verde": "green"})

# Obtener con el metodo
rojo = diccionario.get("rojo")
print("El color rojo es:", rojo)

# Eliminar
del diccionario["rojo"]
diccionario.pop("azul")
print(diccionario)

# Items
print("Items:", diccionario.items())
# Keys
print("Keys:", diccionario.keys())
# Values
print("Values:", diccionario.values())

for value in diccionario.values():
    print(value)
