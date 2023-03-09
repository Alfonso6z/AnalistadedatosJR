from galleta import Galleta


import datetime
def main():
    # fecha_p = datetime.date(2023,3,15)
    g1 = Galleta("Chocolate","Marron",20.0)
    g2 = Galleta("Fresa","Rosa",10.0)
    g3 = Galleta("Vainilla","Amarillo",5.0)
    g4 = Galleta("Arandano","Roja")
    
    # g1.caducidad(fecha_p)
    if g1.morder_galleta()== 0:
        del g1
    if g1.morder_galleta()== 0:
        del g1
    if g1.morder_galleta()== 0:
        del g1
    if g1.morder_galleta()== 0:
        del g1

    print(g1.sabor)
    # g2.morder_galleta()
    # g2.morder_galleta()
    # g2.morder_galleta()
    # g4.morder_galleta()
    # g4.morder_galleta()
    # g4.morder_galleta()
    # g4.morder_galleta()

if __name__ ==  "__main__":
    main()