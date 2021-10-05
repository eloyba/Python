nombres = []
cantidades_nombres = input ("¿Cuanto nombres quieres introducir en la lista?: ")
cantidades_nombres = int(cantidades_nombres)
for numero in range(cantidades_nombres):
    numero_texto = str(numero + 1)
    nombre_elegido = input("Nombre numero "+numero_texto+": ")
    nombres.append(nombre_elegido)
print (nombres)
archivo = open("nombres.txt","w")
for nombre in nombres:
    archivo.write (nombre + "\n")
archivo.close()