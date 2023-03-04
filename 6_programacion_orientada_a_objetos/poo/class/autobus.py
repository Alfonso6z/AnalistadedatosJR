from automovil import Automovil
class Autobus(Automovil):
    
    def capacidad_pasajeros(self,capacidad=50):
        return f"La capacidad es de {self.__nombre} es de {capacidad} pasajeros"
    
    def tarifa(self):
        monto = super().tarifa()
        monto += monto*10/100
        return monto