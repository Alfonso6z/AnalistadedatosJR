
class Galleta:
    
    #! inicializador - constructor 
    # el primer parametro es la referencia a el mismo
    def __init__(self,sabor:str,color:str,peso:float):
        self.sabor = sabor
        self.color = color
        self.peso = peso
        # print(f"Hola soy una galleta de sabor {sabor}")

    def dame_tu_sabor(self)->str:
        return self.sabor
    
    def morder_galleta(self):
        """Cada mordida es de 5.0 si no hay galleta pues me lo notifica
        """
        if self.peso >= 5.0:
            self.peso-=5.0
        elif self.peso>0:
            self.peso = 0
        else:
            print(f"Ya no hay galleta de sabor {self.sabor}")