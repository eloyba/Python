numeros = [1,2,2,3,4,2,2,5,6,7,2]
print (numeros)
cantidad_de_2 = 0
for elemento in numeros:
    if elemento == 2:
        cantidad_de_2 += 1
print ("El 2 esta repetido", cantidad_de_2, "veces")
for i in range (cantidad_de_2):
    numeros.remove(2)
print ("Lista sin el numeros 2:", numeros)