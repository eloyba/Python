numero = input("Elige un numero: ")
noEsnumero = True
while noEsnumero == True:
    try:
        numero = int(numero)
        noEsnumero = False
    except:
        numero = input("No has elegido un numero, elige un numero: ")
print ("Has elegido el:", numero)
numeros = []
numeros_primos = []
num_noPrimos = []
for lista_num in range(0 , numero):
    numeros.append(lista_num+1)
for primos in range(i, numeros):
        if  numeros % primos != 0:
            numeros_primos.append()
        else:
            num_noPrimos.append()
print(numeros)
