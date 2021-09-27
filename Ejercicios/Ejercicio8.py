# Ejercicio 8: Ingresar dos números y mostrar el menor de ellos

nro1 = int(input("Ingresar el primer número: "))
nro2 = int(input("Ingresar el segundo número: "))

if nro1 < nro2:
    print("El primer número es menor que el segundo")
elif nro1 == nro2:
    print("Son iguales")
else:
    print("El segundo número es menor que el primero")
