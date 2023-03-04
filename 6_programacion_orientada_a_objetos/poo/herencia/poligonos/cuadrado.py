from figura import Figura
class Cuadrado(Figura):
    def __init__(self,base):
        super().__init__(4)
        self.base = base
        self.altura = base
    
    def area(self):
        return self.base*self.altura
    
    def perimetro(self):
        return self.base*2 + self.altura*2