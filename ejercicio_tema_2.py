noesnumero = True
minutos = input("Indica los minutos: ")
while noesnumero == True:
    try:
        minutos = int(minutos)
        noesnumero = False
    except:
        minutos = input("No has elegido un numero, elige un numero: ")
segundos = input("Indica los segundos: ")
noesnumero2 = True
while noesnumero2 == True:
    try:
        segundos = int(segundos)
        noesnumero2 = False
    except:
        segundos = input("No has elegido un numero, elige un numero: ")
for tiempo in range(0, minutos+1):
    print(minutos - tiempo)
for sec in range(0, segundos+1):
    print(segundos - sec)