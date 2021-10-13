# Ejercicio 1: Dado un número natural x, mostrar su último dígito.

# Concepto matemático
x = int(input("Ingresa un número natural: "))

if x >= 0:
    ultimo_digito = x % 10
    print("El último dígito es:", ultimo_digito)
else:
    print("Oops!, ingresa un número natural")

# Estilo Python
x = input("Ingresa un número natural: ")
if x.isnumeric():
    print("El último dígito es:", x[-1])
else:
    print("Oops!, ingresa un número natural")
