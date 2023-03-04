class Persona:
    # constructor
    def __init__(self,nombre,apellido,edad,estatura):
        self.__nombre = nombre # get
        self.__apellido = apellido # get
        self.__edad = edad # get y set
        self.__estado_civil = None # get y set
        self.__estatura = estatura # get y set
        print(f"Nacio {nombre}")
    # metodos seteers y geteers
    # def getNombre(self):
    #     return self.__nombre
    
    # def getEdad(self):
    #     return self.__edad
    
    # def getEstatura(self):
    #     return self.__estatura
    # def setEstatura(self,estatura):
    #     self.__estatura = estatura
        
    # def setEstadoCivil(self,persona):
    #     self.estado_civil = persona
    
    @property # get
    def nombre(self):
        return self.__nombre
    
    @property # get
    def apellido(self):
        return self.__apellido
    
    @property
    def estado_civil(self):
        return self.__estado_civil
    @estado_civil.setter
    def estado_civil(self,estado_civil):
        self.__estado_civil = estado_civil
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        self.__edad = edad
    
    @property# get 
    def estatura(self):
        return self.__estatura
    
    @estatura.setter # set
    def estatura(self,valor):
        if valor >= 0.2:
            self.__estatura = valor
        else:
            print("La estatura es incorrecta")

    @estatura.deleter
    def estatura(self):
        del self.__estatura
    
    def saludar(self):
        print(f"Hola soy {self.__nombre}")
    
    def hablar(self,mensaje):
        print(f"{self.__nombre}: {mensaje}")
    
    def esposo(self):
        print(f"esposo: {self.estado_civil.__nombre}")
    
    def __str__(self):
        return f'''
nombre ={self.__nombre}
apellido ={self.__apellido}
edad ={self.__edad}
estado_civil ={self.__estado_civil.nombre if self.__estado_civil != None else "Solter@"}
estatura ={self.__estatura}
'''