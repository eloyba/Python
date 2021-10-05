#primero pedimos una palabra para deletrear
palabra = input("¿Que palabra quieres deletrear?: ")
#ahora se calcula la longitud de la palabra
longitud = len(palabra)
#indicamos que empiece por la posicion 0
posicion = 0
"""indicamos que mientras la posicion de los caracteres sea
inferior o igual a la longitud imprima uno por uno los caracteres de la palabra"""
while posicion + 1 <= longitud:
    print(palabra[posicion])
    posicion = posicion +1