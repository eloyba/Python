def hormigon():
    cantidad = float(input("¿Cuantos metros cubicos de hormigon quieres?: "))
    cemento = 322*cantidad
    arena = 689*cantidad
    grava = 1177*cantidad
    agua = 156*cantidad
    return cemento, arena, grava, agua
materiales = hormigon()
print (materiales)