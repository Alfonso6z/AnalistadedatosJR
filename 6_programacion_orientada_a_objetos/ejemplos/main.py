from galleta import Galleta

def main():
    # instanciar o crear objeto
    g1 = Galleta("Chocolate","Marron",11.0)
    g2 = Galleta("Vainilla","Marron",5.0)

    sabor_g1 = g1.dame_tu_sabor()
    print(sabor_g1)
    # g2 = Galleta("Vainilla","Amarillo")
    # g3 = Galleta("Fresa","Rosa")

    # print(f"esta galleta tiene un sabor de {g3.sabor}")
    # print(f"esta galleta tiene un color {g1.color}")
    
    # print(type(g1))
    
    # g1.dame_tu_sabor()
    # g2.dame_tu_sabor()
    
if __name__ == "__main__":
    main()