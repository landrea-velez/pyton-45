# Ejercicio 3: Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.

x = int(input("Ingresar un número natural: "))

pares = 0
impares = 0

# Concepto matemático
if x >= 0:
    while(x > 0):
        digito = x % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        x = x // 10
    print("La cantidad de digitos pares son:", pares)
    print("La cantidad de digitos impares son:", impares)
else:
    print("Ingresa un número natural")

# Python - Método 1

x = input("Ingresar un número natural: ")
pares = 0
impares = 0

for digito in x:
    if int(digito) % 2 == 0:
        pares += 1
    else:
        impares += 1
print("La cantidad de digitos pares son:", pares)
print("La cantidad de digitos impares son:", impares)
