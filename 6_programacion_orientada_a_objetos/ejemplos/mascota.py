from animal import Animal

class Mascota(Animal):
    
    def __init__(self,nombre,especie, dieta, habitad, f_trasladar,duenio=None):
        # super es referencia a la clase padre
        super().__init__(especie, dieta, habitad, f_trasladar)
        # agregar mis propios atributos 
        self.nombre = nombre
        self.duenio = duenio
    
    def camina(self):
        print(f"soy {self.nombre} y {self.f_trasladar}")