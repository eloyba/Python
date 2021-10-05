archivo = open("nombres2.txt", "r")
nombres = []
for linea in archivo:
    linea = linea.replace("\n", "")
    linea = linea.replace("[", "")
    linea = linea.replace("]", "")
    linea = linea.replace("'", "")
    linea = linea.replace("'", "")
    linea = linea.split(",")
    for elemento in linea:
        nombres.append(elemento)
archivo.close()
print (nombres)