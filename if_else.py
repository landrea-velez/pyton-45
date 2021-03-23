# Teoria: condiciones

numero = int(input("Ingresa un numero: "))

if numero >= 5 and numero < 10:
    print("Es mayor que cinco y menor que diez")
elif numero > 5 and numero > 10:
    print("Es mayor que cinco y mayor que diez")

if numero == 10:
    print("Es igual a 10")
    
if numero == 5:
    print("Es igual a 5")
else:
    print("Es menor que 5 y 10")
