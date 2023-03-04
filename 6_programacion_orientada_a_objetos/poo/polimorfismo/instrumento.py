class Instrumento:
    def __init__(self,tipo,marca,clasificacion):
        self.tipo = tipo
        self.marca = marca
        self.clasificacion = clasificacion
    
    def getTipo(self):
        return self.tipo
    
    def getMarca(self):
        return self.marca