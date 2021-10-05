import random
def euromillones(lista):
    archivo = open("euromillones.txt","a")    
    for i in lista:
        archivo.write(i)
    archivo.write("\n")
    archivo.close()

numeros = []
cantidad = 5
for numero1 in range(cantidad):
    aleatorio = random.randint(1 , 50)
    while aleatorio in numeros:
        aleatorio = random.randint(1 , 50)
    numeros.append(aleatorio)
numeros = str(numeros)
euromillones(numeros)
estrellas = []
cantidad_est = 2
for numero2 in range(cantidad_est):
    aleatorio = random.randint(1 , 12)
    while aleatorio in estrellas:
        aleatorio = random.randint(1 , 12)
    estrellas.append(aleatorio)
estrellas = str(estrellas)
euromillones(estrellas)