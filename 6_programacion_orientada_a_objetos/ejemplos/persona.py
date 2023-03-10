from animal import Animal
class Persona:
    # inicializador
    def __init__(self,nombre:str,edad:int,sexo:str,mascota:Animal=None,conyuge=None):
        self.__nombre:str = nombre
        self.__edad:int = edad
        self.__sexo:str = sexo
        self.__mascota:Animal = mascota
        self.__conyuge:Persona = conyuge

    # dame nombre
    def getNombre(self):
        return self.__nombre
    
    # mascota
    def setMascota(self,mascota):
        self.__mascota = mascota
        
    def getMascota(self):
        return self.__mascota
    # comportamiento
    def hablar(self,mensaje:str):
        print(f"{self.__nombre}: {mensaje}")
        
    def saludar(self):
        print(f"Hola soy {self.__nombre}")
    
    def adoptar_mascota(self,mascota:Animal):
        self.__mascota = mascota
        self.__mascota.duenio = self
        print(f"Adopte un {mascota.especie} y se llama {mascota.nombre}")
    
    def casar_con(self,conyuge):
        self.__conyuge = conyuge
        print(f"Me case con {conyuge.nombre}")