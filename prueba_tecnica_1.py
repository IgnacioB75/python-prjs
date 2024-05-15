''' 
Simulación de prueba técnica utilizando Python
+ sumar_lista() -> toma una lista de números como argumento y devuelve la suma de todos los números de esta
+ fibonacci_recursivo() -> toma 'n' entero como argumento y devuelve el enésimo término de la secuencia fibonacci utilizando recursividad
+ es_palindromo() -> devuelve True si la cadena es palíndroma, y False en caso contrario
+ comprobar_parentesis() -> toma una expresión matemática como argumento. Devuelve True si los paréntesis están balanceados y False en caso contrario
'''

lista_numeros = [2,5,7,1] 
n = 1 

def sumar_lista():
    global lista_numeros
    suma_num = 0
    for num in lista_numeros:
        suma_num = suma_num + num 
        
    print(f'La suma de los números es: {suma_num}')

def fibonacci_recursivo():
    global n
    
    nuevo_num = n # numero que se agrega a la lista
    secuencia = 10
    fibonacci = [0] # [1, 1, 2 ,3 ,5 , 8 ,13 ,21] 
    
    for i in range(secuencia):
        estado_lista = len(fibonacci) - 1 # longitud lista - 1

        n1 = fibonacci[estado_lista]
        fibonacci.append(nuevo_num) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        nuevo_num = nuevo_num + n1
    print(fibonacci)

def es_palindromo():   
    cadena = "radar" # "radar" | "python"
    cadena = cadena.lower()
    
    if cadena == cadena[::-1]: # [::-1] revertir palabra
        return True
    else: 
        return False

def comprobar_parentesis(expresion):
    pila = []  # Creamos una pila vacía para rastrear los paréntesis abiertos

    # Iteramos sobre cada carácter en la expresión
    for char in expresion:
        if char == '(':
            pila.append(char)  # Si encontramos un paréntesis de apertura, lo agregamos a la pila
        elif char == ')':
            if not pila:  # Si encontramos un paréntesis de cierre pero la pila está vacía, la expresión está desbalanceada
                return False
            else:
                pila.pop()  # Si encontramos un paréntesis de cierre y hay un paréntesis de apertura en la pila, lo eliminamos de la pila

    return not pila  # Si la pila está vacía al final, significa que todos los paréntesis están balanceados

sumar_lista() # 15 ✅
fibonacci_recursivo() # 1, 1, 2, 3, 5, 8, 13, 21 ✅
print(es_palindromo()) # test: radar | python ✅
print(comprobar_parentesis("(2+3)*(4-1)")) # test: (2+3)*(4-1) | ((2+3)*(4-1) ✅
