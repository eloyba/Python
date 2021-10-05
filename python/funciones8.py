'''def media(*numeros):
    acumulado = 0
    for numero in numeros:
        #recorro el arbitrario y voy almacenando el valor acumulado
        acumulado = acumulado + numero
        #Divido la suma de todos los numeros que contiene el arbitrario entre su longitud
    media = acumulado/len(numeros)
    return media
#aplico la funcion a unos numeros concretos
miMedia = media(6,7,8,1,5,1)
print ("La media es", miMedia)'''

#usar una lista
numeros = [1,5,6,3,6,4]
def calcular_media(lista):
    acumulado = 0
    for i in lista:
        acumulado = acumulado + i
    media = acumulado/len(lista)
    return media
resultado = calcular_media(numeros)
print ("La media de", numeros, "es", resultado)