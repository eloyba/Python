class Estancia:
    def __init__(self, material_suelo, color_suelo, material_paredes, color_paredes, material_techo, color_techo):
        self.material_suelo = material_suelo
        self.color_suelo = color_suelo
        self.material_paredes = material_paredes
        self.color_paredes = color_paredes
        self.material_techo = material_techo
        self.color_techo = color_techo
    def propiedades(self):
        print ("El material del suelo es", self.material_suelo, "y su color", self.color_suelo)
        print ("El material de las paredes es", self.material_paredes, "y su color", self.color_paredes)
        print ("El material del techo es", self.material_techo, "y su color", self.color_techo)