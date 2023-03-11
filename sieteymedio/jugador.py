class Jugador:
    
    def __init__(self,nick,humano,recursos=None):
        self.__nick = nick
        self.__humano = humano
        self.__recursos = recursos
    
    def recursos(self):
        pass
    
    def turno(self):
        pass
    
    def victorias(self):
        pass

    @property
    def nick(self):
        return self.__nick
    @nick.setter
    def nick(self,nick):
        self.__nick = nick
    
    @property
    def humano(self):
        return self.__humano
    @humano.setter
    def humano(self,humano):
        self.__humano = humano
    
    @property
    def recursos(self):
        return self.__recursos
    @recursos.setter
    def recursos(self,recursos):
        self.__recursos = recursos