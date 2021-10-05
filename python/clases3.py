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
#creamos al primer objeto soldado
primer_soldado = Soldado("Eldelbar" , "Elfo")
#imprimimos el nombre y la raza de nuestro soldado
print ("Nombre:")
print (primer_soldado.nombre)
print ("Raza:")
print (primer_soldado.raza)
print ("Vida:")
print (primer_soldado.vida)
print ("Velocidad:")
print (primer_soldado.velocidad)
print ("Coste:")
print (primer_soldado.coste)
#veamos que tipo es la variable primer_soldado
print (type(primer_soldado))