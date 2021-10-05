class Soldado:
    def __init__(self , nombre , raza):
        self.nombre = nombre
        self.raza = raza
        if raza == "Elfo":
            self.vida = 80
            self.velocidad = 10
            self.coste = 200
        elif raza == "Humano":
            self.vida = 100
            self.velocidad = 7
            self.coste = 100
        elif raza == "Enano":
            self.vida = 120
            self.velocidad = 3
            self.coste = 180
ejercito = []
noEsnumero = True
num_soldados = input("¿Cuantos soldados quieres crear?: ")
while noEsnumero == True:
    try:
        num_soldados = int(num_soldados)
        noEsnumero = False
    except:
        num_soldados = input("No es un numero, elige un numero: ")
for numero in range(num_soldados):
    nombre_elegido = input("Escribe un nombre: ")
    raza_elegida = input("Escribe una raza: ")
    soldados_creados = Soldado(nombre_elegido , raza_elegida)
    ejercito.append(soldados_creados)
for i in range(len(ejercito)):
    print (ejercito[i].nombre)