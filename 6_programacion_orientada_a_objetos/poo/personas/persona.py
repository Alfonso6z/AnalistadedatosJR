class Persona:
    # constructor
    def __init__(self,nombre,apellido,edad,estatura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estado_civil = None
        self.estatura = estatura
        print(f"Nacio {nombre}")
    
    def saludar(self):
        print(f"Hola soy {self.nombre}")
    
    def hablar(self,mensaje):
        print(f"{self.nombre}: {mensaje}")
    
    def estadoCivil(self,persona):
        self.estado_civil = persona
    
    def esposo(self):
        print(f"esposo: {self.estado_civil.nombre}")
    
    def __str__(self):
        return f'''
nombre ={self.nombre}
apellido ={self.apellido}
edad ={self.edad}
estado_civil ={self.estado_civil.nombre}
estatura ={self.estatura}
'''