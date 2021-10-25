# Ejercicio 25
"""
Se debe generar los primeros k números de la serie de Fibonacci. En la serie
los dos primeros números son el 0 y el 1. El resto se calcula como la suma de los dos
números que lo preceden. Además debe contar cuantos números primos existen en la serie
generada
"""

k = int(input("Ingresar K: "))
a = 0
b = 1
c_primos = 0
while(a < k):
    cx = 0
    if a != 0:
        for divisor in range(1, a+1):
            if a % divisor == 0:
                cx += 1
        if cx <= 2:
            c_primos += 1
    print(a)
    a, b = b, a+b
print("Cantidad de primos:", c_primos)
