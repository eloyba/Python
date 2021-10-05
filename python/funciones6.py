'''def hormigon():
    cantidad = float(input("¿Cuantos metros cubicos de hormigon quieres?: "))
    materiales = []
    cemento = 322*cantidad
    materiales.append(cemento)
    arena = 689*cantidad
    materiales.append(arena)
    grava = 1177*cantidad
    materiales.append(grava)
    agua = 156*cantidad
    materiales.append(agua)
    return materiales
materiales = hormigon()
print (materiales)'''

#mejora del codigo anterior
'''def hormigon():
    cantidad = float(input("¿Cuantos metros cubicos de hormigon quieres?: "))
    cantidad_por_metro = [322,689,1177,156]
    materiales = []
    for i in range(len(cantidad_por_metro)):
        materiales.append(cantidad_por_metro[i]*cantidad)
    return materiales
materiales = hormigon()
print (materiales)'''

#otra opcion con diccionario
def hormigon():
    cantidad = float(input("¿Cuantos metros cubicos de hormigon quieres?: "))
    cantidad_por_metro = [322,689,1177,156]
    tipo_material = ["cemento" , "arena" , "grava" , "agua"]
    materiales = {}
    for i in tipo_material:
        materiales[i] = cantidad_por_metro[tipo_material.index(i)]*cantidad
    return materiales
materiales = hormigon()
print (materiales)