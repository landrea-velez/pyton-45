# variables Tipado dinamico

nombre= "Laura"
edad = 32
altura = 1.60
CONSTANTE = "HOLA"
print("mi nombre es ", nombre, " ", edad)
print(CONSTANTE)


# tipos de datos
# String -> cadena de caracteres -> str
print("Que tipo de dato es 'hola':", type("hola"))

# Integer -> numeros entero 1 2 3 4 -1 - 2 -3 
# int
numero = 1
print("Que tipo de dato es 243", type(numero))

# Float -> numeros con deciames 1.2 3.4 -3.3 3.14 
# float
numero_float = 23.1
print("Que tipo de dato es 23.1", type(numero_float))

# Boolean -> verdaderos o falsos -> bool
# True = es verdadero
# False = es falso
# True = 1
# False = 0 
booleano = True
print("Que tipo de dato es True", type(booleano))



# Teoria: cadenas de texto

# Declarar
texto = "soy un texto" 
texto = 'soy un texto'
texto = """soy un texto"""
texto = '''soy un texto'''

# Resaltar o combinar comillas
print("hol'a'")
print('hol"a"')

# Formateo
nombre = "Laura"
apellido = "Velez"
edad = 21

print("Hola, mi nombre es: {0} {1} {2}".format(nombre, apellido, edad))
#print(f"Hola, mi nombre es {nombre} {apellido} y mi edad es {edad}")

# Concatenar
nombre_completo = nombre + " " + apellido
print("Mi nombre completo es:", nombre_completo)

# Slicing
palabra = "hola"
print("Letra:", palabra[0]) # h
print("Letra:", palabra[1]) # o
print("Letra:", palabra[2]) # l
print("Letra:", palabra[3]) # a

print("Negativo:", palabra[-1])
print("Negativo:", palabra[-2])
print("Negativo:", palabra[-3])
print("Negativo:", palabra[-4])

print("Todos:", palabra[:])
print("Negativo:", palabra[::-1])

# Metodos
palabra = "chau"
palabra = palabra.replace("c", "g")
print(palabra)
print(palabra.capitalize())
print(palabra.find("h"))
print(palabra.upper())

# metodo split

palabra = "hola soy un texto"
print(palabra.split())