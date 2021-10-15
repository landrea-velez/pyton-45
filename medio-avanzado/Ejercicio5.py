# Ejercicio 5: Dado un número natural x, determinar si es capicúa.

# Concepto matemático
print("---- Concepto matemático ----")
x = int(input("Ingresar número natural: "))

auxiliar = x
capicua = 0

while(x > 0):
    ultimo = x % 10
    capicua = (capicua * 10) + ultimo
    x = x // 10
if capicua == auxiliar:
    print("Es capicua")
else:
    print("No es capicua")

# Python - con range
print("---- Con la función range ----")

x = input("Ingresar número natural: ")
lista = []
for digito in range(len(x)-1, -1, -1):
    lista.append(x[digito])
capicua = "".join(lista)
if x == capicua:
    print("Es capicua")
else:
    print("No es capicua")


# Python - Metodo fácil y rápido
print("---- Con slicing ----")

x = input("Ingresar número natural: ")
if x == x[::-1]:
    print("Es capicua")
else:
    print("No es capicua")
