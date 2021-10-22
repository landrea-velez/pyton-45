# Ejercicio 19: Dado un número natural, calcular su factorial.

x = int(input("Ingresar N: "))

if x >= 0:
    factorial = 1
    for c in range(1, x+1):
        factorial *= c
    print("Factorial:", factorial)
else:
    print("Ingresa un número natural")
