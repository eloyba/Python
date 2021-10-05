numeros = [1,2,3,4]
numeros.remove(2)
print (numeros)
numeros = [1,2,3,4]
numeros.remove(numeros[1])
print (numeros)
numeros = [1,2,3,2,4,2,2]
numeros.remove(2)
print (numeros)
numeros = [1,2,3,4]
del numeros[2]
print (numeros)
numeros = [1,2,3,4]
del numeros[numeros.index(2)]
print (numeros)
numeros = [1,2,3,4,5,6]
del numeros[1:4]
print (numeros)
numeros = [1,2,3,4,5,6]
del numeros[3:]
print (numeros)
numeros = [1,2,3,4,5,6]
del numeros[:]
print (numeros)