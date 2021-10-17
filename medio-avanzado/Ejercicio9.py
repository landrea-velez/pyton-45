# Ejercicio 9: Dado un número natural x, sumar todos sus divisores.

x = int(input("Ingresar X: "))

sumador = 0
c = 1
while(c < x):
    if x % c == 0:
        sumador += c
    c += 1
print("Resultado con while:", sumador)

sumador = 0
for c in range(1, x):
    if x % c == 0:
        sumador += c
print("Resultado con for:", sumador)
