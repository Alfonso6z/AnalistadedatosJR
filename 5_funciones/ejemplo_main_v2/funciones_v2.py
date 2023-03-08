
def suma_n_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma+=numero
    return suma

def promedio_n_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma+=numero
    return suma

def maximo_minimo(numeros):
    maximo = numeros[0]
    minimo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
        if numero<minimo:
            minimo = numero
    return maximo,minimo