from marcas_modelos import marcas_motos

# Ingresar marca y modelo:
marca = input("Ingresa la marca de la motocicleta: ")
modelo = input("Ingresa el modelo de la motocicleta: ")

if marca.upper() in marcas_motos and modelo.upper() in marcas_motos[marca.upper()]:
    # 'marca.upper()'verifica si existe la marca (en mayúsuclas) en el diccionario de 'marcas_modelos'
    # Si la marca existe, procede a verificar si el modelo existe, entra en marcars_motos y devuelve (con [marca.upper()]) la información del modelo
    
    informacion = marcas_motos[marca.upper()][modelo.upper()] # Accede a la información de marcas_motos[marca][modelo] (estos datos se almacenan en mayúsculas)
    print(f"Información de la motocicleta {marca.upper()} {modelo.upper()}:") # Imprime la información almacenada en 'marca' y 'modelo'

    for clave, valor in informacion.items():
        print(f"{clave.capitalize()}: {valor}") # Por ejemplo '{Motor}: {4 tiempos}' 
else:
    print("No se encontró información para la motocicleta especificada.") # Error si no se encuentra
