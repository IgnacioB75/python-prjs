'''
Crear un programa que traduzca números decimales a:
Binario💻
'''
def convertidor_binario(n):
    # Lista para almacenar los dígitos binarios
    binario = []

    # Manejo del caso especial cuando n es 0
    if n == 0:
        binario = [0]

    while n > 0:
        # Calcula el resto
        resto = n % 2

        # Agrega el dígito binario al principio de la lista
        binario.insert(0, resto)

        # Divide n por 2 (reseteo)
        n = n // 2 

    # Convierte la lista de dígitos binarios a una cadena
    binario_str = ''.join(map(str, binario))

    return binario_str

# Prueba con el número 20
decimal_numero = int(input("Ingrese el número decimal "))
binario_resultado = convertidor_binario(decimal_numero)
print(f"El número {decimal_numero} en binario es: {binario_resultado}")