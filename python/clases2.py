class Soldado:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        print ("He sido creado para servirle, a sus ordenes, soy un" ,self.raza, "y me llamo" , self.nombre)
soldado1 = Soldado("Eldelbar", "Elfo")