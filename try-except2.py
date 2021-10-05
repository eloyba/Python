print ("Vamos a sumar dos numeros")
numero_1 = input("¿Cual es el primer numero?: ")
numero_2 = input("¿Cual es el segundo numero?: ")
try:
    numero_1 = int(numero_1)
except:
    numero_1 = input("No has elegido un numero, elige un numero: ")
    numero_1 = int(numero_1)
try:
    numero_2 = int(numero_2)
except:
    numero_2 = input("No has elegido un numero, elige un numero: ")
    numero_2 = int(numero_2)
suma = numero_1 + numero_2
suma = str(suma)
print ("La suma de ambos numeros es "+ suma)