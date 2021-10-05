noesnumero = True
numero_1 = input("Di un numero: ")
while noesnumero == True:
    try:
        numero_1 = int(numero_1)
        noesnumero = False
    except:
        numero_1 = input("No has elegido un numero, elige un numero: ")
numero_2 = input("Di un segundo numero: ")
noesnumero2 = True
while noesnumero2 == True:
    try:
        numero_2 = int(numero_2)
        noesnumero2 = False
    except:
        numero_2 = input("No has elegido un numero, elige un numero: ")
print("Puedes elegir los siguientes numeros:")
print("1 - Sumar ambos numeros")
print("2 - Restar ambos numeros")
print("3 - Multiplicar ambos numeros")
print("4 - Dividir ambos numeros")
seleccion = input("¿Cual es tu eleccion?: ")
if seleccion == "1":
    print(numero_1 + numero_2)
elif seleccion == "2":
    print(numero_1 - numero_2)
elif seleccion == "3":
    print(numero_1 * numero_2)
elif seleccion == "4":
    print(numero_1 / numero_2)
else:
    print("Nos has elegido ninguna de las opciones")