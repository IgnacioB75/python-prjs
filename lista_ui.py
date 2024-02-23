import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Función para agregar un elemento a la lista
def agregar_elemento():
    elemento = entry_elemento.get()
    if elemento.strip() != '':
        lista.append(elemento)
        actualizar_historial()

# Función para actualizar el historial con los elementos de la lista
def actualizar_historial():
    historial.config(state=tk.NORMAL)
    historial.delete(1.0, tk.END)
    for elemento in lista:
        historial.insert(tk.END, f"{elemento}\n")
    historial.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Listado")
ventana.geometry("800x600")
ventana.configure(bg="#ececec")

# Crear lista para almacenar elementos
lista = []

# Crear entrada de texto para ingresar elementos
entry_elemento = ttk.Entry(ventana)
entry_elemento.pack(pady=10)

# Crear botón para agregar elemento
boton_agregar = ttk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Crear historial de elementos
historial = ScrolledText(ventana, height=20, width=50)
historial.pack(pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()
