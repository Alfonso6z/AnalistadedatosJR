from figura import Figura
class Triangulo(Figura):
    
    def __init__(self,base,altura):
        super().__init__(3)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base*self.altura)/2
    
    def perimetro(self):
        return 3*self.base