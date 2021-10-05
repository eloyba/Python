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
    print ("La suma de los dos numeros es", suma)
while terminamos == 0:
    print ("Nuestras opciones:")
    print ("1. Realizr un suma")
    print ("2. Terminar")
    pregunta = input("¿Que quieres hacer? (1 o 2): ")
    if pregunta == "1":
        #llamo a la funcion
        funcionSuma()
    elif pregunta == "2":
        print ("Adios")
        terminamos = 1