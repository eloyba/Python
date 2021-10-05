material = []
noEsnumero = True
cantidad_material = input("¿Cuantos materiales vas a usar?: ")
while noEsnumero == True:
    try:
        cantidad_material = int(cantidad_material)
        noEsnumero = False
    except:
        cantidad_material = input("No has elegido un numero, elige un numero: ")
for numero in range(cantidad_material):
    numero_texto = str(numero + 1)
    material_elegido = input("Escribe un material: ")
    material.append(material_elegido)
#print (material)
cantidades = []
for cantidad in range(cantidad_material):
    cantidad_texto = str(cantidad + 1)
    cantidad_elegido = input("Escribe una cantidad: ")
    noesNumero = True
    while noesNumero == True:
        try:
            cantidad_elegido = int(cantidad_elegido)
            noesNumero = False
        except:
            cantidad_elegido = input("No has elegido un numero, elige un numero: ")
    cantidad_elegido = str(cantidad_elegido)
    cantidades.append(cantidad_elegido)
#print (cantidades)
diccionario = dict(zip(material, cantidades))
#print (diccionario)
archivo = open("materiales.txt","a")
for clave, valor in diccionario.items():
    archivo.write(clave +" --> " + valor + "\n")
archivo.close()