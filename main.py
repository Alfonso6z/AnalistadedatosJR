def agrega_nombre(i,alumnos):
    while True:
        nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
        if nombre not in alumnos:
            break
        print(f"{nombre} ya existe")
    return nombre

def agregar_notas():
    notas = []
    cont = 1
    while True:
        try:
            nota = float(input(f"Ingresa la nota {cont}: "))
            if nota<0:
                break
            if nota in range(11):
                notas.append(nota)
                cont+=1
            else:
                print("NO esta en el rango [0,10]")
        except:
            print("Error:  Ingresa números !!!!")
    return notas

def imprime_alumnos(alumnos):
    print("Nombre\tNotas")
    for alumno,notas in alumnos.items():
        print(f"{alumno}:\t{notas}")
    print("Termine ...")

def notas_alumnos():
    alumnos = {}
    while True:
        try:
            n = int(input("Ingresa el número de alumnos: "))
            break
        except:
            print("Error: ingresa un número")
            
    for i in range(n):
        # verifica si existe
        nombre = agrega_nombre(i,alumnos)
        # crear notas
        notas = agregar_notas()
        alumnos[nombre]=notas
    return alumnos

def main():
    imprime_alumnos(notas_alumnos())

if __name__ == "__main__":
    main()