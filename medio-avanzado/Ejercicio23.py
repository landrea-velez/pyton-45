# Ejercicio 23
""" 
Calcular cuantos segundos tiene una hora dada. (por ej. 12:23:15 tiene 44595
segundos)
"""

hora = int(input("Ingresar la hora: "))
minutos = int(input("Ingresar los minutos: "))
segundos = int(input("Ingresar segundos: "))

resultado = (hora * 3600) + (minutos * 60) + segundos

print("Resultado:", resultado)
