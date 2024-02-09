from marcas_modelos import marcas_motos, sinonimos_marcas, sinonimos_modelos

# Ingresar marca y modelo:
marca_ingresada = input("Ingresa la marca de la motocicleta: ")
modelo_ingresado = input("Ingresa el modelo de la motocicleta: ")

marca_valida = None
modelo_valido = None

def verificar_marca():
    global marca_valida
    for marca,sinonimos in sinonimos_marcas.items():
        if marca_ingresada.upper() in sinonimos:
            marca_valida = marca
            print("Marca valida")
            break
        else:
            print("Modelo inválido")
            break

def verificar_modelo():
    global modelo_valido
    for modelo, sinonimos in sinonimos_modelos.items():
        if modelo_ingresado.upper() in sinonimos:
            modelo_valido = modelo
            print("Modelo válido")
            break
        else:
            print("Modelo inválido")
            break

verificar_marca()
verificar_modelo()

def validar_marca_modelo():
    print(f'estado marca: {marca_valida}')
    print(f'estado modelo: {modelo_valido}')
    
    if marca_valida and modelo_valido:
        print("marca y modelo válidos")
        return True
    else:
        print("marca y/o modelo inválido/s")
        return False

def info_motocicleta():
    if validar_marca_modelo():
        informacion = marcas_motos[marca_valida][modelo_valido]
        print(f"Información de la motocicleta {marca_valida.capitalize()} {modelo_valido}:")
        for clave, valor in informacion.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("No se encontró información para la motocicleta especificada.")

info_motocicleta()