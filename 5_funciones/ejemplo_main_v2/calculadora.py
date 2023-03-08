''' importar todas las funciones de funciones'''
# from funciones import suma_n_numeros
''' importar todo el archivo y darle un alias'''
import funciones as f
import funciones_v2 as f2
import os
# !definición no ejecuta la función

def desplegar_menu(numeros:list)->float:
    """Muestra el menú de la calculadora

    Args:
        numeros (list): lista de números ingresados por el usuario

    Returns:
        float: resultado de la operacción eljida
    """
    while True:
        opt = f.menu(
            "Calculadora",                             #* titulo
            "suma_n_numeros",                          #? opt
            "promedio_n_numeros",                      #?
            "maximo_minimo",                           #?
            "segundos_a_minutos",                      #?
            "calcula_hora",                            #?
            "ingresar otros números",                  #?
            "Salir",                                   #? opt
            error="Opción invalida intentalo de nuevo",#! keyword
            primera_vez=True)                         #! keyword
        if opt!=-1 and opt!=6:
            break
        if opt == 6:
            numeros = ingresar_datos()
        input("Enter para continuar ...")
    return selecciona_opcion(opt,numeros)

def selecciona_opcion(opcion:int,numeros:list)->float:
    """Realiza la operación selecciona en el menú

    Args:
        opcion (int): la opción
        numeros (list): lista de números ingresados por el usuario

    Returns:
        float: valor de la operación, -1 si es salir
    """
    if opcion == 1:
        return f2.suma_n_numeros(numeros)
    elif opcion == 2:
        return f2.promedio_n_numeros(numeros)
    elif opcion == 3:
        return f2.maximo_minimo(numeros)
    elif opcion == 4:
        return f.segundos_a_minutos(90)
    elif opcion == 5:
        return f.calcula_hora(15,0,0,125)
    else:
        return -1

def ingresar_datos()->list:
    """Pide los números enteros al usuario rango variable

    Returns:
        list: lista con los números ingresados por usuario
    """
    numeros_i = []
    cont = 1
    while True:
        n = int(input(f"Ingresa el número {cont}, -1 para terminar: "))
        if n == -1:
            return numeros_i
        numeros_i.append(n)
        cont+=1

def iniciar():
    """Inicia el programa de calculadora
    """
    os.system("cls")
    numeros = ingresar_datos()
    while True:
        os.system("cls")
        salida = desplegar_menu(numeros)
        if salida == -1:
            break
        print(salida)
        input("Enter para continuar ...")
        while True:
            os.system("cls")
            opt = f.menu("Continuar","Si","No",error="solo elige 1 o 2",primera_vez=False)
            if(opt != -1):
                break
        if opt == 2:
            break
    print("Adios ... |m|")