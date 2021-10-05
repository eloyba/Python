numero = int(input("Elige un numero: "))
if numero%2 == 0:
    #si hemos entrado es porque el numero es par
    if numero > 9:
        print("El numero elegido es par y mayor a 9")
    else:
        print("El numero elegido es par y menor o igual que 9")
else:
    #si hemos entrado es porque es impar
    if numero > 9:
        print("El numero es impar y mayor que 9")
    else:
        print("El numero es impar y menor o igual que 9")
