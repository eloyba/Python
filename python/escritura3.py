import random
cantidad = input ("¿Cuantos nombres quieres introducir aleatoriamente en la lista?: ")
cantidad = int(cantidad)
aleatorios = []
for numero in range(cantidad):
    aleatorio = random.randint(1 , cantidad)
    while aleatorio in aleatorios:
        aleatorio = random.randint(1 , cantidad)
    aleatorios.append(aleatorio)
nombres = []
for i in range(cantidad):
    nombrenumero = str(i+1)
    nombre = input("Nombre "+nombrenumero+": ")
    nombres.append(nombre)
print (aleatorios)
print (nombres)
diccionario = {}
for i in range(len(aleatorios)):
    diccionario[nombres[i]] = aleatorios[i]
print (diccionario)