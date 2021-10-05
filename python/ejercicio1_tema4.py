nombres = []
intencion = input ("¿Quieres introducir mas nombres en la lista existente o quieres \n empezar una nueva lista? (1: Mas nombres, 2: Nueva lista): ")
cantidades_nombres = input ("¿Cuanto nombres quieres introducir en la lista?: ")
cantidades_nombres = int(cantidades_nombres)
for numero in range(cantidades_nombres):
    numero_texto = str(numero + 1)
    nombre_elegido = input("Nombre numero "+numero_texto+": ")
    nombres.append(nombre_elegido)
print (nombres)
if intencion == "1":
    nom_archivo = input("¿Que archivo quieres usar?: ")
    existe = True
    while existe == True and nom_archivo == True:
        try:
            archivo = open(nom_archivo,"a")
            for nombre in nombres:
                archivo.write (nombre + "\n")
            archivo.close()
            existe = False
        except:
            archivo = input("Ese archivo no existe, elige otro: ")
elif intencion == "2":
    archivo = input("¿Que archivo quieres usar?: ")
    while archivo == True:
        try:
            archivo = open("prueba.txt","w")
            for nombre in nombres:
                archivo.write (nombre + "\n")
            archivo.close()
        except:
            archivo = input("Ese archivo no existe, elige otro: ")
   