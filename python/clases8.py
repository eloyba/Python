class Soldado:
    def __init__(self, nombre, raza, sueldo):
        self.nombre = nombre
        self.raza = raza
        self.__sueldo = sueldo
        #sueldo esta oculto, se puede accerder usando print(mi_soldado._Soldado__sueldo)
    def arma(self, arma):
        self.arma = arma
        print ("Muchas gracias, ahora tengo un/una", self.arma)