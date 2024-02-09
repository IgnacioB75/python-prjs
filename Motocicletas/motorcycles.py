from marcas_modelos import marcas_motos, sinonimos_marcas, sinonimos_modelos

# Ingresar marca y modelo:
marca_ingresada = input("Ingresa la marca de la motocicleta: ")
modelo_ingresado = input("Ingresa el modelo de la motocicleta: ")

marca_valida = None
modelo_valido = None

def verificar_marca():
    global marca_valida
    for marca, sinonimos in sinonimos_marcas.items():
        if marca_ingresada.upper() in sinonimos:
            marca_valida = marca
            print("Marca válida")
            return True
    print("Marca inválida")
    return False

def verificar_modelo():
    global modelo_valido
    for modelo, sinonimos in sinonimos_modelos.items():
        if modelo_ingresado.upper() in sinonimos:
            modelo_valido = modelo
            print("Modelo válido")
            return True
    print("Modelo inválido")
    return False

def info_motocicleta():
    if verificar_marca() and verificar_modelo():
        informacion = marcas_motos[marca_valida][modelo_valido]
        print(f"Información de la motocicleta {marca_valida.capitalize()} {modelo_valido}:")
        for clave, valor in informacion.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("No se encontró información para la motocicleta especificada.")

info_motocicleta()