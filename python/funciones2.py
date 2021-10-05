def hormigon():
    cantidad = float(input("¿Cuantos metros cubicos de hormigon quieres?: "))
    cemento = 322*cantidad
    arena = 689*cantidad
    grava = 1177*cantidad
    agua = 156*cantidad
    print ("Necesitas las siguientes cantidades:")
    print (cemento, "kilogramos de cemento")
    print (arena, "kilogramos de arena")
    print (grava, "kilogramos de grava")
    print (agua, "kilogramos de agua")
hormigon()
#aqui da error porque la variable cemento esta dentro de la funcion y la estamos llamando desde fuera
print ("Vamos a imprimir la variable cemento tras terminar la funcion")
print (cemento)