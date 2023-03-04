from persona import Persona
def main():
    p1 = Persona("Omar", "Cruz", 25, 1.80)
    p2 = Persona("Lupe", "González", 22, 1.78)
    
    p1.saludar()
    
    p1.hablar(f"Hola {p2.nombre}!")
    p2.hablar(f"Que tal {p1.nombre}!")
    
    p1.estadoCivil(p2)
    p2.estadoCivil(p1)
    
    print(p1)
    print(p2)
    
    
if __name__ == "__main__":
    main()