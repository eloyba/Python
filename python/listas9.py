numeros = [1,2,2,3,4,2,2,5,6,7,2]
print (numeros)
nueva_lista = []
for elemento in numeros:
    if elemento != 2:
        nueva_lista.append(elemento)
print (nueva_lista)
del numeros