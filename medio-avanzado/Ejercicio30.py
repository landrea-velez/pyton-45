# Ejercicio 30:
"""
Dada una tabla que contiene los artículos y precios de un negocio y cantidad de stock, 
simular generar una factura de a lo sumo 6 artículos, e
n la cual el usuario solo debe ingresar el artículo y la cantidad 
(revisar que el art. tenga stock). El programa debería calcular los subtotales y 
el total general de la factura.
"""
from tabulate import tabulate

matriz = [
    ["Artículos", "Precios", "Stock"],
    ["Celulares", 400, 20],
    ["Tablets", 500, 40],
    ["Sillas", 200, 200],
    ["Mesas", 500, 20],
    ["Kiwis", 30, 1000],
    ["Manzanas", 15, 0],
    ["Peras", 12, 5]
]
print(tabulate(matriz, headers='firstrow'))

n = len(matriz)  # cantidad de filas
m = len(matriz[0])  # cantidad de columnas
carrito = [
    ["Artículo", "Precio", "Stock", "Subtotal"],
]

while(True):
    print(""" --- Selecciona una opción ---
    [1] Seleccionar artículo
    [2] Mostrar artículos en el carrito
    [3] Realizar venta
    [4] Mostrar productos
    [5] Salir
    """)
    opcion = input("Ingresar opción: ")
    if opcion.isnumeric():
        if opcion == "1":
            articulo = input("Ingresar nombre del artículo: ")
            cantidad = int(input("Ingresar cantidad: "))
            if cantidad > 0:
                for fila in range(1, n):
                    if matriz[fila][0].lower() == articulo.lower():
                        if matriz[fila][2] >= cantidad:
                            matriz[fila][2] -= cantidad
                            carrito.append(
                                [matriz[fila][0],
                                 matriz[fila][1],
                                 cantidad,
                                 matriz[fila][1] * cantidad
                                 ]
                            )
                        else:
                            print(
                                "El stock es menor que la cantidad, no se puede vender.")
            else:
                print("Ingresa una cantidad mayor que cero")
        elif opcion == "2":
            if len(carrito) > 1:
                print(tabulate(carrito, headers='firstrow'))
            else:
                print("El carrito está vacío")
        elif opcion == "3":
            if len(carrito) > 1:
                total = 0
                for producto in range(1, len(carrito)):
                    total += carrito[producto][3]
                print("El total es:", total)
            else:
                print("El carrito no tiene productos, no se puede vender nada.")
        elif opcion == "4":
            print(tabulate(matriz, headers='firstrow'))
        elif opcion == "5":
            break
        else:
            print("Ingresa una opción correcta.")
    else:
        print("Ingresa una opción correcta.")
