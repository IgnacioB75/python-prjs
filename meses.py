# Arrays
meses_30 = [ 4, 6, 9, 11] # Meses que tienen 30 días
meses_31 = [ 1, 3, 5, 7, 8, 10, 12] # Meses que tienen 31 días
meses = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] # Array de los meses del año

def dias_mes():
    if numero_mes in meses_30:
        return 30
        # print("El mes tiene 30 días")
    elif numero_mes in meses_31:
        return 31
        # print("El mes tiene 31 días")
    elif numero_mes == 2:
        return 28
        # print("El mes es febrero")
    else:
        return None
        # print("Número de mes no válido")

while 1: # "while 1" = Si el programa inicia (1 = ON)
    try: # El programa intenta iniciar la función, si no puede pasa a 'except'
        print(f"\n") # Salto de línea en consola
        numero_mes = int(input("Ingresa un número de mes (1-12): "))  # Input del número del mes
        print("El número del mes introducido es:", numero_mes)  # Mostrarle al usuario su elección

        if 1 <= numero_mes <= 12:
            print("-------------------------------------")
            
            # Función
            dias_mes()

            print(f"El mes es {meses[numero_mes - 1]} y tiene {dias_mes()} días")  # Imprime el nombre del mes seleccionado
            
            print("-------------------------------------")
            break  # Termina el bucle si no hay errores

        else:
            print("-------------------------------------")
            print("Error: Ingresa un número entre 1 y 12")
            print("-------------------------------------")

    except ValueError: # Si la función no se pudo iniciar, lanza ValueError
        print("Error: Ingresa un número válido") # Mensaje de Error
        retry = input("¿Quieres intentarlo de nuevo? (s/n): ") # Mensaje para saber si el usuario quiere intentarlo denuevo

        if retry.lower() != 's': # Si el usuario presiona tecla distinta a "s", se termina el bucle | .lower() escribe el input en letras minúsculas
            break  # Termina el bucle si el usuario no quiere intentarlo de nuevo

# Testing: numero_mes = -1|0|2|4|5|13 