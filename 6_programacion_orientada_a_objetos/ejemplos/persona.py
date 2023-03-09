from animal import Animal
from persona import Persona
class Persona:
    # inicializador
    def __init__(self,nombre:str,edad:int,sexo:str,mascota:Animal=None,conyuge:Persona=None):
        pass
    
    # comportamiento
    def hablar(self,mensaje:str):
        pass
    
    def saludar(self):
        pass
    
    def adoptar_mascota(self,mascota:Animal):
        pass
    
    def casar_con(self,conyuge:Persona):
        pass