from art import *

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
    
def segundos_a_minutos(seg):
    m = seg // 60
    s = seg % 60
    return m,s
    
def calcula_hora(horas_a,minutos_a,segundos_a,tiempo):
    horas_s = horas_a*60*60
    minutos_s = minutos_a*60
    tiempo_s = horas_s+minutos_s+segundos_a
    tiempo = tiempo+tiempo_s
    
    segundos_b = tiempo%60
    minutos_aux = tiempo//60
    minutos_b = minutos_aux%60
    horas_aux = minutos_aux//60
    horas_b = horas_aux%24
    dias = horas_aux//24
    
    return dias,horas_b,minutos_b,segundos_b


# https://pypi.org/project/art/
def arte_ascii(titulo,opt):
    # rnd-xlargew hite_bubble block'
    # Art=text2art("< EDC >",font='rnd-xlargew',chr_ignore=True)
    return  tprint(titulo,"rand") if opt == 1 else tprint(titulo,"rdn")