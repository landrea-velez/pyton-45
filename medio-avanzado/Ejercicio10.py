# Ejercicio 10: Dados dos números naturales A y B, mostrar sus divisores comunes

a = int(input("Ingresar A: "))
b = int(input("Ingresar B: "))

if a >= 0 and b >= 0:
    c = 1
    mayor = 0
    if a > b:
        mayor = a
    else:
        mayor = b
    print("Divisores comunes: ", end="")
    while(c < mayor):
        if a % c == 0 and b % c == 0:
            print(c, end=" ")
        c += 1

# Set y list

divisores_a = []
divisores_b = []

for c in range(1, a):
    if a % c == 0:
        divisores_a.append(c)

for c in range(1, b):
    if b % c == 0:
        divisores_b.append(c)

interseccion = list(set(divisores_a) & set(divisores_b))

print("Divisores comunes:", interseccion)
