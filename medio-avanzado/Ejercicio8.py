# Ejercicio 8: Dado un número natural x, mostrar todos sus divisores.

x = int(input("Ingresar X: "))

c = 1
print("Divisores: ", end="")
while(c < x):
    if x % c == 0:
        print(c, end=" ")
    c += 1


print("Divisores: ", end="")
for c in range(1, x):
    if x % c == 0:
        print(c, end=" ")
