numero = input("Elige un numero: ")
try:
    numero = int(numero)
except:
    numero = input("Nos has elegido un numero, elige un numero: ")
    numero = int(numero)
if numero % 2 == 0:
    print("Has elegido un numero par")
if numero % 2 == 1:
    print("Has elegido un numero impar")