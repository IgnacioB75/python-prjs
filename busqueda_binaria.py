''' Busqueda binaria en Python 🐍 '''

import random
import os

# Variables 
num = random.randint(1,100) # Número por adivinar
intentos = 0 
control = 0 # Controlar funcionamiento
lista = [] # Lista de números ingresados

# Juego de adivinar número entre 1 y 100    
while (control == 0):
    print(f'Intento número: {intentos}')
    
    n = int(input()) # Número a comparar

    os.system("cls") # Borra el terminal 

    # Si adivinó el número
    if (n == num):
        print("Adivinaste el número!")
        print(f'Utilizaste {intentos} intentos.')
        control += 1
    elif (n > num):
        print("El número ingresado es MAYOR, intenta nuevamente")
        intentos += 1
    elif (n < num):
        print("El número ingresado es MENOR, intenta nuevamente")
        intentos += 1
    
    lista.append(n) # Agrega a la lista el número ingresado
    print(f'Números ingresados: {lista}') # Muestra la lista de números ingresados

def datos():
    print(" ")
    print("- Datos del programa -")
    print(f'Número aleatorio: {num}')
    print(f'Intentos: {intentos}')

datos()