lista_numeros = []
noEsnumero = True
numero = input("Indica la cantidad de numeros a almacenar: ")
while noEsnumero == True:
    try:
        numero = int(numero)
        noEsnumero = False
    except:
        numero = input("No has elegido un numero, indica un numero: ")
print ("Has elegido el:", numero)
for i in range(0, numero):    
    lista_numeros.append(i+1)
print (lista_numeros)
    