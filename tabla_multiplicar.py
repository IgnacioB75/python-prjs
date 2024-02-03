# Tabla de multiplicar personalizable

def tabla_multiplicar(numero, limit):
    for i in range(0,limit):
        multiplicacion = i + 1
        valor = (numero * multiplicacion)
        print(f'{numero} x {multiplicacion} = {valor}')  

while True:
    try:
        numero = int(input("ingresa un número: "))
        limit = int(input("Ingrese el rango de multiplicación (a partir del 0): "))
        
        if (numero >= 0):
            tabla_multiplicar(numero,limit)
            break  
    
    except ValueError:
        print("Por favor, ingrese un número válido.")
        retry = input("¿Quieres volver a intentarlo? (S/N): ")
        if retry.lower() != 's':
            break
        print(f"\n")
    finally:
        print("¡Gracias por usar el programa!")