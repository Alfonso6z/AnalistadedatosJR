from persona import Persona
def main():
    p1 = Persona("Oscar", "González", 18, 1.50)
    print(p1.nombre)
    print(p1.estatura)
    p1.estatura = 0
    print(p1.estatura)
    del p1.estatura
    print(p1.estatura)

if __name__ == "__main__":
    main()