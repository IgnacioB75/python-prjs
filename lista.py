import os
import keyboard
import time

lista = []

def ingresar_elemento():
    elemento = str(input("Nombre del elemento: "))
    if elemento.strip() == '' or elemento.lower() == 'q':
        return False
    lista.append(elemento)
    print(len(lista))
    os.system("cls")
    return True

def mensaje_stop():
    if len(lista) == 1:
        print(f'La longitud de la lista es de {len(lista)} elemento')
    else:
        print(f'La longitud de la lista es de {len(lista)} elementos')
    
    print(lista)
    print("Se terminó el bucle")

def main():
    os.system("cls")
    while True:
        if not ingresar_elemento():
            mensaje_stop()
            break
        time.sleep(0.1)

# Programa que muestra un listado con los elementos que ingrese el usuario
if __name__ == '__main__':
    main()