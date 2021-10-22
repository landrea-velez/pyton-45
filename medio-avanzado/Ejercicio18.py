# Ejercicio 18: Dados 3 números naturales, A, B y C, mostrar los múltiplos de A,
# menores que B que no sean divisores de C

a = int(input("Ingresar A: "))
b = int(input("Ingresar B: "))
c = int(input("Ingresar C: "))

for i in range(1, a+1):
    resultado = a % i
    if resultado == 0 and i < b and c % i != 0:
        print("Número que cumple las condiciones:", i)
