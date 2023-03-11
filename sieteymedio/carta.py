class Carta:
    
    def __init__(self,figura,valor):
        self.__figura = figura
        self.__valor = valor
        
    @property
    def figura(self):
        return self.__figura
    
    @property
    def valor(self):
        return self.__valor
    
    def __str__(self):
        return f"({self.__figura},{self.__valor})"