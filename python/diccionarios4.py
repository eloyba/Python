lista1 = ["Ana","Maria","Juan"]
lista2 = [23, 30, 43]
diccionario = {}
for i in lista1:
    diccionario[i] = lista2[lista1.index(i)]
print (diccionario)		