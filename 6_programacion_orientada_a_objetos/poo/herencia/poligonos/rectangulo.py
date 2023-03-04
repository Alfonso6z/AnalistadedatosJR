from cuadrado import Cuadrado
from figura import Figura
class Rectangulo(Cuadrado,Figura):
    
    def __init__(self,base,altura):
        super().__init__(4)
        self.base = base
        self.altura = altura