from triangulo import Triangulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo
def main():
    t1 = Triangulo(15, 18)
    print(t1.lados)
    print(t1.area())
    print(t1.perimetro())
    
    c1 = Cuadrado(4)
    print(c1.area())
    
    r1 = Rectangulo(4, 6)
    print(r1.area())
    print(r1.perimetro())
    
if __name__ == "__main__":
    main()