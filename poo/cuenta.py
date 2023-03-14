"""Ejercicio 2. (2 puntos) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.

mostrar(): Muestra los datos de la cuenta.

ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""
from persona import Persona
class Cuenta:
    # constructor
    def __init__(self,titular:Persona,cantidad:float=0.0):
    # atributos
        self.__titular = titular
        self.__cantidad = cantidad
        pass
    # comportamientos
    def ingresar(self,cantidad):
        try:
            if cantidad > 0:
                self.__cantidad+=cantidad
        except:
            print("La cantidad a ingresar tiene que ser un número")
            
    def retirar(self,cantidad):
        try:
            if cantidad <= self.cantidad:
                self.__cantidad-=cantidad
        except:
            print("La cantidad a retirar tiene que ser un número")
            
    def mostrar(self):
        return f"""titular:{self.titular.nombre}
cantidad:{self.cantidad}
    """

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    
    @property
    def cantidad(self):
        return self.__cantidad