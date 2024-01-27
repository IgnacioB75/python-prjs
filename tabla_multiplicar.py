'''
* Crea un programa que sea capaz de solicitarte un número y se
* encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
* - Debe visualizarse qué operación se realiza y su resultado.
*   Ej: 1 x 1 = 1
*       1 x 2 = 2
*       1 x 3 = 3
*       ... 
 '''

numero = int(input("Ingresa el número para multiplicar "))
print("El número introducido es: ",numero)

if (numero >= 0):
    for i in range(10):
        multiplicacion = i + 1
        #print(multiplicacion)
        #print("______________________")
        valor = (numero * multiplicacion)
        print(numero, "x", multiplicacion, "=", valor)
else:
    print("No es un número válido")