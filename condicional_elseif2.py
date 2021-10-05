numero_1 = input("Elige el primer numero: ")
try:
    numero_1 = int(numero_1)
except:
    numero_1 = input("No has elegido un numero, elige el primer numero: ")
    numero_1 = int(numero_1)
numero_2 = input("Elige el segundo numero: ")
try:
    numero_2 = int(numero_2)
except:
    numero_2 = input("No has elegido un numero, elige el segundo numero: ")
    numero_2 = int(numero_2)
print("Puedes elegir los siguientes numeros:")
print("1 - Sumar ambos numeros")
print("2 - Restar ambos numeros")
seleccion = input("¿Cual es tu eleccion?: ")
if seleccion == "1":
    print(numero_1 + numero_2)
elif seleccion == "2":
    print(numero_1 - numero_2)
else:
    print("Nos has elegido ninguna de las opciones")