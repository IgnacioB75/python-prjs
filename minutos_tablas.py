import time
import os
from tabulate import tabulate

# Variables al iniciar el contador
dia = 0
hora = 0
minutos = 0
segundos = 0

while True: # Función que se ejecuta al iniciar el programa
    segundos = segundos
    segundos += 1

    if segundos >= 60: # Minutos
        minutos = minutos
        minutos += 1
        segundos = 0
    if minutos >= 60: # Horas
        hora = hora
        hora += 1
        minutos = 0
        segundos = 0
    if hora >= 24: # Días
        hora = 0
        minutos = 0
        segundos = 0
        dia += 1
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    table = [[f'{hora:0>2}',
              f'{minutos:0>2}',
              f'{segundos:0>2}']] # Contenido de la tabla | la cadena f'{hora:0>2}' sirve para darle formato al texto, en estos casos si no tiene 2 dígitos dice >>> 00 
    headers = ["hora", "minutos", "segundos"] # Título del contenido en la tabla
    
    print("hora:", f'{hora:0>2}', "minutos:", f'{minutos:0>2}',"segundos:", f'{segundos:0>2}') # Imprimir los contadores + formato
    print(tabulate(table, headers, tablefmt="simple_grid")) # Imprimir la tabla // Intercambiable con los prints(línea 43-48)

    if dia >= 1: # Cuándo pase un día, empezará a aparecer el contador
        print("Días transcurridos:",dia) 

    time.sleep(1) # Tiempo antes de incrementar el contador en segundos
    os.system("cls") # Limpia la terminal
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - 