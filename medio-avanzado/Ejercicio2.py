# Ejercicio 2: Dado un número natural x, contar la cantidad de dígitos que posee.

x = int(input("Ingresar un número natural: "))

# Concepto matemático
c = 0
if 0 <= x < 10:
    print("La cantidad de digitos son: 1")
else:
    while x > 0:
        c += 1
        x = x // 10
    print("La cantidad de dígitos son:", c)

# Python - Metodo 1
x = input("Ingresar un número natural: ")

if x.isnumeric():
    print("La cantidad de dígitos son:", len(x))
else:
    print("oops!, ingresa un número natural")

# Python - Metodo 2
c = 0
for digito in x:
    c += 1
print("La cantidad de dígitos son:", c)
