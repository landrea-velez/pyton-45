# Teoria: while, ciclo condicional

numero = 1
while(numero < 5):
    algo = input("ingresa algo: ")
    numero = numero + 1
print("Se termino")


############################## Teoria: ciclo for (ciclo incondicional)
lista = [1,2,3,4,5]
tupla = (1,2,3,4)
diccionario = {1:1, 2:2, 3:3}
texto = "hola"
numero = str(12345)

# Iterador - iteracion
"""for letra in texto:
    print("Letra:", letra)"""

# Con rangos
"""for numero in range(-5, 6, 2):
    print(numero)"""

# Enumeracion
for enumerador, valor in enumerate(texto):
    print("La posicion es:", enumerador)
    print("Y la letra es:", valor)

# break
for numero in range(30):
    if numero == 25:
        break
    print(numero)

    for a in range(10):
    print(a-1)