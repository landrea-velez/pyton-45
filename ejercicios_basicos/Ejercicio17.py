# Ejercicio 17: Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingresa una frase: ")
letra = input("Ingresa la letra: ")

contador = 0
largo = len(frase)
c = 0
while(c < largo):
    if frase[c] == letra:
        contador += 1
    c += 1
print("La letra ingresada aparece", contador, "veces")
print("-----------")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra ingresada aparece", contador, "veces")
