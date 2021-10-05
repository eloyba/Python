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
    def arma(self, arma):
        self.arma = arma
        print ("Muchas gracias, ahora tengo un", self.arma)
primer_soldado = Soldado("Eldelbar" , "Elfo")
primer_soldado.arma("Arco")
#creamos mas soldados
segundo_soldado = Soldado("Bran" , "Humano")
segundo_soldado.arma("Espada")
tercer_soldado = Soldado("Gloin" , "Enano")
tercer_soldado.arma("Hacha")
