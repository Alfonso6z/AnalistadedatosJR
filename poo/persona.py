"""Ejercicio 1. (2 puntos) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y dni. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona:
    
    def __init__(self,nombre:str="",edad:int=0, dni:str=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def montrar(self):
        return f"""nombre:{self.nombre}
edad:{self.edad}
dni:{self.dni}
    """
    
    def es_mayor_de_edad(self):
        return self.edad >17
        

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre:str):
        nombre_valido = True
        # verifica si es un número
        if str(nombre).isdigit():
            print("No puedes colocar digitos")
            return None
        # verifica si tiene un numero // 41f0n50
        for caracter in nombre:
            if str(caracter).isdigit():
                print("Tu nombre no puede contener números")
                return None
        # acturliza
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad:int):
        try:
            aux_edad = int(edad)
            if edad>0:
                self.__edad = edad
            else:
                print("la edad debe ser positiva")
        except:
            print("Edad tiene que ser entero")
    
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,dni):
        if str(dni).isdigit():
            return None
        if len(dni) == 13:
            self.__dni = dni