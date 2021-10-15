# Ejercicio 4: Dado un número natural x, sumar todos sus dígitos. Mostar la suma obtenida.


# Concepto matemático
x = int(input("Ingresar un número natural: "))

sumador = 0

while(x > 0):
    digito = x % 10
    sumador += digito
    x = x // 10
print("El resultado es:", sumador)


# Python - Método 1
x = input("Ingresar un número natural: ")
sumador = 0
for digito in x:
    sumador += int(digito)
print("El resultado es:", sumador)

# Python - Método 2
x = input("Ingresar un número natural: ")
lista = []
for digito in x:
    lista.append(int(digito))
print("El resultado es:", sum(lista))
