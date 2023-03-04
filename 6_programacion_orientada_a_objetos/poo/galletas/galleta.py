# definir una clase con la palabra reservada class
class Galleta():
    #contructor o instanciador
    # def __init__(self,nombre,sabor,color,gramos): <- atributos obligatorios
    def __init__(self,nombre,sabor="Chocolate",color="Cafe",gramos=5.0): # gramos no es obligatorio
        # atributos de los objetos
        self.nombre = nombre
        self.color = color
        self.sabor = sabor
        self.gramos = gramos
    
    # comportamiento
    def mordida(self):
        if self.gramos > 0:
            self.gramos-=2.5
        else:
            print("Ya no hay galleta")
    
    # 
    def cuantaGalleta(self):
        if self.gramos<0:
            print(f"No hay galleta")
        else:
            print(f"Hay {self.gramos}g de galleta")

    # imprimir objeto aplicando un print()
    def __str__(self):
        return f'''
nombre = {self.nombre}
color = {self.color}
sabor = {self.sabor}
gramos = {self.gramos}\n
    '''