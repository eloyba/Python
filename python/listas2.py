noEsnumero = True
nombres = []
cantidad_nombres = input("¿Cuantos nombres quieres?: ")
while noEsnumero == True:
    try:
        cantidad_nombres = int(cantidad_nombres)
        noEsnumero = False
    except:
        cantidad_nombres = input("No has elegido un numero, elige un numero: ")
#print (cantidad_nombres)
for numero in range(cantidad_nombres):
    numero_texto = str(numero + 1)
    nombre_elegido = input("Escribe un nombre: ")
    nombres.append(nombre_elegido)
print(nombres)