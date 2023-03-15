from jugador import Jugador
from carta import Carta
class JugadorSiete(Jugador):
    
    def __init__(self, nick, humano,recursos:dict):
        super().__init__(nick, humano,recursos)
        self.__mano:list = recursos["mano"]
        self.__puntos:float = recursos["puntos"]
    
    def agregar_carta(self,carta:Carta):
        self.__mano.append(carta)
    
    def contar_puntos(self):
        self.__puntos = 0
        for carta in self.__mano:
            self.__puntos+=carta.valor
        return self.puntos
    
    def mostrar_mano(self):
        m_cartas:str = ""
        for carta in self.__mano:
            m_cartas+=f"({carta.figura},{carta.valor})\n"
        return m_cartas
    
    def __str__(self):
        return f"""nickname: {self.nick}
humano:{self.humano}
puntos:{self.puntos}"""
    
    @property
    def mano(self):
        return self.__mano
    @mano.setter
    def mano(self,mano):
        self.__mano = mano
        
    @property
    def puntos(self):
        return self.__puntos
    @puntos.setter
    def puntos(self,puntos):
        self.__puntos = puntos
