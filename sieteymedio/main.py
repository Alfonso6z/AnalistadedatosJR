import cartas

def main():
    baraja = cartas.crear_cartas()
    print(baraja[0])
    print(type(baraja[0]))
    print(baraja[0].valor)
    print(type(baraja[0].valor))
    print(baraja[0].figura)
    print(type(baraja[0].figura))
    
if __name__ == "__main__":
    main()