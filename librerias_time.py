import time
tiempo = input("¿Cuanto tiempo tendra la cuneta atras?: ")
tiempo = int(tiempo)
while tiempo >= 0:
    print(tiempo)
    tiempo = tiempo - 1
    time.sleep(1)