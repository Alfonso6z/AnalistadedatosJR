class Automovil:
    def __init__(self,nombre,velocidad_max,kilometraje,capacidad):
        self.__nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
        self.capacidad = capacidad
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def en_marcha(self,km):
        self.kilometraje+=km
        return self.kilometraje
    
    def capacidad_pasajeros(self):
        return f"La capacidad de {self.__nombre} es de {self.capacidad} pasajeros"
    
    def tarifa(self):
        return self.capacidad * 100