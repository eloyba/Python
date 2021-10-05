class Soldado:
    #definimos el constructor, es decir, la funcion __init__
    #situamos los parametros que queremos y el obligado self al principio
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
#creo mi primer soldado e indico que es de la clase Sodado
#creamos un elfo llamado eldelbar
soldado1 = Soldado("Eldelbar", "Elfo")
#imprimimos el nombre y la raza del nuestro soldado
print (soldado1.nombre)
print (soldado1.raza)