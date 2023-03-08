''' importar todas las funciones de funciones'''

# from funciones import menu

''' importar todo el archivo y darle un alias'''

import funciones as f
import funciones_v2 as f2
import sys
# def main():
#     opt = f.menu("Calculadora", # titula 
#             "suma_n_numeros",     # opt
#             "promedio_n_numeros",
#             "maximo_minimo",
#             "segundos_a_minutos",
#             "calcula_hora",
#             "salir",              # opt
#             error="Elegiste la opción incorrecta",# kword
#             primera_vez = True)# kword
    
#     if opt == 1:
#         suma_n = f.suma_n_numeros(56,89,7)
#         print("suma_n = ",suma_n)
#     elif opt == 2:
#         promedio = f.promedio_n_numeros(45,2,5)
#         print("promedio = ",promedio)
#     elif opt == 3:
#         max_min = f.maximo_minimo(1,5,9,87,7)
#         print("max_min = ",max_min)
#     elif opt == 4:
#         seg,minutos = f.segundos_a_minutos(90)
#         print("seg = ",seg)
#         print("minutos = ",minutos)
#     elif opt == 5:
#         hora = f.calcula_hora(15,0,0,90)
#         print("hora = ",hora)
#     elif opt == 6:
#         print("salir")
#     else:
#         print("no existe")    
def main(numeros):
    titulo = f2.arte_ascii("calculadora", 2)
    while True:
        opt = f.menu(titulo, # titula 
                "suma_n_numeros",     # opt
                "promedio_n_numeros",
                "maximo_minimo",
                "segundos_a_minutos",
                "calcula_hora",
                "ingresa numeros",
                "salir",              # opt
                error="Elegiste la opción incorrecta",# kword
                primera_vez = True)# kword
        if opt == 1:
            suma_n = f2.suma_n_numeros(numeros)
            print("suma_n = ",suma_n)
        elif opt == 2:
            promedio = f2.promedio_n_numeros(numeros)
            print("promedio = ",promedio)
        elif opt == 3:
            max_min = f2.maximo_minimo(numeros)
            print("max_min = ",max_min)
        elif opt == 4:
            seg,minutos = f.segundos_a_minutos(numeros[0])
            print("seg = ",seg)
            print("minutos = ",minutos)
        elif opt == 5:
            hora = f.calcula_hora(numeros[0],numeros[1],numeros[2],numeros[3])
            print("hora = ",hora)
        elif opt == 6:
            numeros = f.input_n_numeros()
        elif opt == 7:
            break
        else:
            print("no existe")
        input("\nEnter para continuar ...")

    print("Termine .... \n Adios .. ")

if __name__ == "__main__":
    aux = sys.argv.copy()
    aux.pop(0)
    numeros = [int(numero) for numero in aux]
    main(numeros)