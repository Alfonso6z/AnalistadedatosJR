def usuario_decorador(): # funcion decoradora
    def super_usuario(cls): # funcion interna o funcion b
        class SuperUsuario(cls): # clase o funcio c, hereda de la clase que se recive por parametro
            def nombre_completo(self):
                return f"{self.nombre} {self.apellido}"
            def __str__(self):
                return f"Hola, mi nombre completo es: {self.nombre_completo()}"
        return SuperUsuario # retorna la funcion interna o funcion b
    return super_usuario # retorna la funcion decoradora

@usuario_decorador()
class Usuario:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

@usuario_decorador()
class Alumno:
    def __init__(self,nombre,apellido,grupo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__grupo = grupo
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @property
    def grupo(self):
        return self.__grupo
    @grupo.setter
    def grupo(self,grupo):
        self.__grupo = grupo
    
def main():
    u1 = Usuario("Juan", "Hernadez")
    print(u1.nombre_completo())
    print(u1)
    
    a1 = Alumno("Pedro", "González", "A1B2C3")
    print(a1)
if __name__ == "__main__":
    main()