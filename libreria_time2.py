import time
noesnumero = True
tiempo = input("¿Cuanto tiempo tendra la cuenta atras?: ")
while noesnumero == True:
    try:
        tiempo = int(tiempo)
        noesnumero = False
    except:
        tiempo = input("No has elegido un numero, elige un numero: ")
while tiempo >= 0:
    print(tiempo)
    tiempo = tiempo - 1
    time.sleep(1)
print("Cuenta atras terminada")