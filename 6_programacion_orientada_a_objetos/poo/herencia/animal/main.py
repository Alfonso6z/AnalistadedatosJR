from animal import Animal
from mascota import Mascota
from cocodrilo import Cocodrilo
def main():
    a1 = Animal("Elefante")
    print(a1.especie)
    m1 = Mascota("Gato")
    print(m1.especie)
    c1 = Cocodrilo("especie")
if __name__ == "__main__":
    main()