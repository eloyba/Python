terminamos = 0
#creo mi funcion
def funcionSuma():
    #pregunto los numeros
    numero1 = input("Primer numero: ")
    numero2 = input("Segundo numero: ")
    #los conviernto en enteros
    numero1 = int(numero1)
    numero2 = int(numero2)
    #Sumo los numeros y los imprimo
    suma = numero1 + numero2
    #Devuelvo la suma de los numeros
    return numero1 + numero2
while terminamos == 0:
    print ("Nuestras opciones:")
    print ("1. Realizr un suma")
    print ("2. Terminar")
    pregunta = input("¿Que quieres hacer? (1 o 2): ")
    if pregunta == "1":
        #llamamos la funcion suma y la almacenamos en la variable suma
        suma = funcionSuma()
    elif pregunta == "2":
        print (suma)
        print ("Adios")
        terminamos = 1