from animal import Animal
from mascota import Mascota
from persona import Persona

def main():
    p1 = Persona("Benjamin", 18, "M")
    p2 = Persona("Maria", 20, "F")
    p3 = Persona("Raul", 30, "M")
    m1 = Mascota("Firulais", "Perro", "Croquetas", "Dept", "correr")
    
    print(p1.getNombre())
    print(m1.nombre)
    p1.adoptar_mascota(m1)
    print(p1.getMascota().duenio.getNombre())


if __name__ == "__main__":
    main()