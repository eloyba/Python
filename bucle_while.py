noesnumero = True
numero_1 = input("Di un numero: ")
while noesnumero == True:
    try:
        numero_1 = int(numero_1)
        noesnumero = False
    except:
        numero_1 = input("No has elegido un numero, elige un numero: ")
print("El numero elegido es:", numero_1)