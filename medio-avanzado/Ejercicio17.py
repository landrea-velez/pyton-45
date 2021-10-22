# Ejercicio 17: Dado un número natural, mostrar el mayor de sus dígitos.

# Concepto matemático

mayor = -1
numero = int(input("Ingresar número: "))
while(numero > 0):
    if numero % 10 > mayor:
        mayor = numero % 10
    numero = numero // 10

print("El mayor es:", mayor)

# Python
mayor = -1
numero = input("Ingresar número: ")
print("EL mayor es:", max(numero))
