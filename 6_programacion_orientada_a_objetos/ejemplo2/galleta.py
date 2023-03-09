import datetime 
class Galleta:
    #! Atributos o caracteristicas
    #? Comportamientos
    
    #* Inicializador o constructor
    def __init__(self,sabor,color,peso=12.0,fecha:datetime = datetime.date.today()):
        self.sabor = sabor
        self.color = color
        self.peso = peso
        self.f_creacion = fecha
        self.f_vigencia = datetime.date(fecha.year,fecha.month,fecha.day+5)

    def caducidad(self,fecha_hoy:datetime.date):
        if (fecha_hoy.day-self.f_creacion.day)>=5:
            print("caducado :(")
        else:
            print("vigente")
            
    def morder_galleta(self):
        if self.peso>=5.0:
            self.peso-=5.0
            return self.peso
        elif self.peso>0:
            self.peso = 0
            return self.peso
        else:
            print(f"Ya no hay galleta de {self.sabor}:(")
            return -1