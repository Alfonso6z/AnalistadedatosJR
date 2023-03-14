from persona import Persona
from cuenta import Cuenta
def main():
    p1 = Persona("Raul",21,"ASDFKASDJGIASDFAD")
    # p1.nombre = "Ricardo"
    # p1.edad = 18
    # p1.dni = "GOZA910625306"
    # print("-----Actualización-----")
    # print(p1.montrar())
    # print(p1.es_mayor_de_edad())
    
    c1 = Cuenta(p1)
    c1.ingresar(200.0)
    c1.retirar("fsdf")
    print(c1.mostrar())
if __name__ == "__main__":
    main()