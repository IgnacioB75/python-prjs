''' 
Condiciones para que un número sea primo:
1. Ser un número natural mayor que uno
2. Ser divisible por 1 && ser divisible por si mismo
3. No ser divisible por cualquier otro número natural aunque de decimal  

Contador de primos:
- Pedirle al usuario la cantidad de números primos que desea ver
- Añadir números primos a una lista de la misma longitud que el número ingresado por el usuario
- Mostrar la lista (de menor a mayor) con los números primos (sin el 0 ni el 1)
'''
# Primeros 5 números primos: 2, 3, 5, 7 y 11
cantidad = int(input("Ingrese la cantidad de números primos que desea ver: "))

def es_primo(numero):
    if numero <= 1: # 1 no es primo
        return False
    elif numero <= 3: # 2 y 3 son primos
        return True
    elif (numero % 2) == 0 or (numero % 3) == 0: # Si divisible por 2 o 3 no es primo
        return False
    
    i = 5
    while i * i <= numero: # cuando raíz cuadrada de i (5 * 5 = 25) es menor o igual al número...
        if numero % i == 0 or numero % (i + 2) == 0: # Si el numero es divisible por i o por i + 2, no es primo
            return False
        i += 6 # Aumentamos i en 6 para saltar los múltiplos de 2 y 3

    return True # La función devuelve True si ninguna de las condiciones anteriores se cumple

def generar_primos(cantidad):
    lista_primos = []
    numero = 2 # primero número primo

    while len(lista_primos) < cantidad: # Mientras la longitud de la lista no sea la deseada...
        if es_primo(numero): # Si es True ...
            lista_primos.append(numero) # Añadir al final de lista_primos(): numero
        numero += 1 # Sumar 1 en cada repetición
    
    return lista_primos # Devuelve lista_primos en la funció

primos = generar_primos(cantidad)
print(f'Lista de primos: {primos}')
# Contador primos