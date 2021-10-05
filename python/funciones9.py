cantidad = input("¿De cuantos valores necesitas hacer la media?: ")
cantidad = int(cantidad)
valores = []
def calcular_media(lista):
    acumulado = 0
    for i in lista:
        acumulado = acumulado + i
    media = acumulado/len(lista)
    return media
for i in range(cantidad):
    i = str(i + 1)
    valor = input("valor numero "+i+": ")
    #Convertimos a float por si el usuario introduce un numero decimal
    valor = float(valor)
    valores.append(valor)
resultado = calcular_media(valores)
print ("La media de", valores, "es", resultado)