from animal import Animal
class Persona:
    # inicializador
    def __init__(self,nombre:str,edad:int,sexo:str,mascota:Animal=None,conyuge=None):
        self.__nombre:str = nombre
        self.__edad:int = edad
        self.__sexo:str = sexo
        self.__mascota:Animal = mascota
        self.__conyuge:Persona = conyuge
    
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
    
    # get es cuando retorna una variable privada
    @property
    def nombre(self):
        return self.__nombre
    # set actualiza una variable privada
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        self.__edad = edad
        
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self,sexo):
        self.__sexo = sexo
    
    @property
    def mascota(self):
        return self.__mascota
    @mascota.setter
    def mascota(self,mascota):
        self.__mascota = mascota
    
    @property
    def conyuge(self):
        return self.__conyuge
    @conyuge.setter
    def conyuge(self,conyuge):
        self.__conyuge = conyuge
""" 
"setYget":{
		"prefix":"setget",
		"body":[
			"@property",
    		"def $CLIPBOARD(self):",
        	"\treturn self.__$CLIPBOARD",
    		"@$CLIPBOARD.setter",
    		"def $CLIPBOARD(self,$CLIPBOARD):",
        	"\tself.__$CLIPBOARD = $CLIPBOARD",
		],
		"description": "Crear setters y getter"
	}
"""