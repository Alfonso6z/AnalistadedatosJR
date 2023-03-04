class Animal:
    
    def __init__(self,especie):
        self.especie = especie
        self.numero_patas = None
        self.alimentacion = None
        self.clase = None
        self.sonido = None

    def comen(self):
        print(f" soy {self.especie} y me alimento de {self.alimentacion}")
    
    def tipoSonido(self):
        print(f"{self.especie}: {self.sonido}")