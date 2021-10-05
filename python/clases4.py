class Soldado:
    def __init__(self , nombre , raza):
        self.nombre = nombre
        self.raza = raza
        #incluyo el arma como variable propia del objeto y vaor inicial vacio
        self.arma = ""
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
primer_soldado.arma = "Arco"
print (primer_soldado.nombre , primer_soldado.raza , primer_soldado.arma)