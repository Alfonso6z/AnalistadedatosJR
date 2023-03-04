''' importar todas las funciones de funciones'''
# from funciones import *
''' importar todo el archivo y darle un alias'''
import funciones as f

def main():
    print("Hola mundo")
    maxi,mini = f.maximo_minimo(1,2,3)
    print(f"maximo = {maxi} , minimo = {mini}")
    
if __name__ == "__main__":
    main()