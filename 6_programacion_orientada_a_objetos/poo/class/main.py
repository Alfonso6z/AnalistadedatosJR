from automovil import Automovil
from autobus import Autobus

def main():
    a1 = Automovil("vw",100,10000,4)
    # a2 = Automovil("ford",200,5000)
    # a3 = Automovil("toyota",150,10000)
    b1 = Autobus("Escolar Volvo", 80, 10000, 50)
    # a1.en_marcha(100)
    
    print(a1.tarifa())
    print(b1.tarifa())

    a1.set_nombre("volkswagen")
    print(a1.get_nombre())
    
if __name__ == "__main__":
    main()