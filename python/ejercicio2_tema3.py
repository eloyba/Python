dicc_materiales = {"cemento" : ["calcio" , "silicio" , "aluminio" , "hierro"], "mortero":["arena" , "cemento" , "agua"], "hormigon":["arena" , "cemento" , "grava" , "agua"]}
print ("Puedes elegir los siguientes elementos:","1-Cemento", "2-Mortero", "3-Hormigon")
elemento = input("Elige uno: ")
noEsnumero = True
while noEsnumero == True:
    try:
        elemento = int(elemento)
        noEsnumero = False
    except:
        elemento = input("No has elegido un numero, elige un numero: ")
elemento = str(elemento)
if elemento == "1":
    print (dicc_materiales["cemento"])
elif elemento == "2":
    print (dicc_materiales["mortero"])
elif elemento == "3":
    print (dicc_materiales["hormigon"])
else:
    print ("Esa no es una opcion")