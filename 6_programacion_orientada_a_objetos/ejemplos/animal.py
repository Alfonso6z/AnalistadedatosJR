class Animal:
    
    def __init__(self,especie:str,dieta:str,habitad:str,f_trasladar:str):
        self.especie = especie
        self.dieta = dieta
        self.habitad = habitad
        self.f_trasladar = f_trasladar

    #comportamientos
    def camina(self):
        print(f"soy un {self.especie} y {self.f_trasladar}")

    def comer(self):
        print(f"{self.especie} y me alimento de {self.dieta}")