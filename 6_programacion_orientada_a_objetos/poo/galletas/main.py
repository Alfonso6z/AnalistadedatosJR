from galleta import Galleta

def main():
    # instanciar un objeto / crear un objeto
    g1 = Galleta("Marinela", "Chocolate", "Cafe")
    g2 = Galleta("Gamesa", "Vainilla", "Amarillo", 8.0)
    # imprimir atributos del objeto g1
    g1.mordida()
    g1.mordida()
    g1.mordida()
    print(g1.gramos)
    
    g2.mordida()
    g2.mordida()
    g2.mordida()
    g2.mordida()
    g2.mordida()
    print(g2.gramos)
    
    g1.cuantaGalleta()
if __name__ == "__main__":
    main()