import cartas
from jugadorSiete import JugadorSiete

def main():
    j1 = JugadorSiete("El albert", True, {"mano":[],"puntos":0.0})
    baraja = cartas.crear_cartas()
    print(j1)
    j1.agregar_carta(baraja.pop())
    j1.agregar_carta(baraja.pop())
    print(j1.mostrar_mano())
    print(j1.contar_puntos())
    print(j1.contar_puntos())

if __name__ == "__main__":
    main()