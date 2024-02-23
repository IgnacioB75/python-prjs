import tkinter as tk

def obtener_input():
    marca = entrada_marca.get()
    modelo = entrada_modelo.get()
    print("marca: ", marca)
    print("modelo: ",modelo)

def contenido(ventana):
    global entrada_marca
    global entrada_modelo

    etiqueta_marca = tk.Label(ventana, text="Marca:", bg="#c5c5c5")
    etiqueta_marca.grid(row=0, column=0, padx=10, pady=10)

    entrada_marca = tk.Entry(ventana)
    entrada_marca.grid(row = 0, column=1, padx=10, pady=10)
    
    etiqueta_modelo = tk.Label(ventana, text="Modelo:", bg="#c5c5c5")
    etiqueta_modelo.grid(row=1, column=0, padx=10, pady=10)

    entrada_modelo = tk.Entry(ventana)
    entrada_modelo.grid(row=1, column=1, padx=10, pady=10)

    boton_obtener = tk.Button(ventana, text="Mostrar Contenido", command=obtener_input)
    boton_obtener.grid(row=2, column=2, padx=10, pady=10)

    return entrada_marca, entrada_modelo

def crear_interfaz():
    # Setup
    ventana = tk.Tk()
    ventana.configure(bg="#ececec")
    ventana.geometry("800x640")
    ventana.title("Busqueda de motocicleta")

    entrada_marca, entrada_modelo = contenido(ventana)

    ventana.mainloop()
    return ventana, entrada_marca, entrada_modelo 