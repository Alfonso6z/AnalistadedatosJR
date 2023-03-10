from acuatico import Acuatico
from terrestre import Terrestre
class Cocodrilo(Acuatico,Terrestre):
    
    def desplazar(self):
        print("Desde cocodrilo")
        super().desplazar()
        super().desplazar()