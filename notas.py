import tkinter as tk
from tkinter import filedialog

ruta_archivo = ''

''' Funciones '''
# Menu -> Archivo
def nuevo_archivo():
    textarea.delete(1.0, tk.END) # Borrar area de texto al ejecutar la función

def abrir_archivo():
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension=".txt", filetype=[
        ("Archivos de textos", "*.txt"),
        ("Archivos de python", "*.py"),
        ("Todos los archivos", "*.*")])
    
    textarea.delete(1.0, tk.END) # Borrar area de texto al ejecutar la función

    with open(ruta_archivo, "r", encoding="UTF-8") as file: # "r" es para que lo habra en tipo lectura (read)
        textarea.insert(tk.INSERT, file.read())
    
def guardar_archivo():
    global ruta_archivo
    if ruta_archivo:
        try:
            with open(ruta_archivo, "w", encoding="UTF-8") as file: # "w" para que escriba en el archivo (write)
                file.write(textarea.get(1.0, tk.END))
        except:
            print("No se puede guardar el archivo")

def guardar_como():
    nueva_ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetype=[
        ("Archivos de textos", "*.txt"),
        ("Archivos de python", "*.py"),
        ("Todos los archivos", "*.*")])
    
    if nueva_ruta:
        with open(ruta_archivo, "w", encoding="UTF-8") as file: # "w" para que escriba en el archivo (write)
                file.write(textarea.get(1.0, tk.END))

# Menu -> Edición
def copiar():
    textarea.event_generate(("<<Copy>>"))

def cortar():
    textarea.event_generate(("<<Cut>>"))

def pegar():
    textarea.event_generate(("<<Paste>>"))

''' Ventana '''
ventana = tk.Tk()
ventana.title("Notas ✏")
ventana.geometry("800x600")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo)

edicion = tk.Menu(menu)
menu.add_cascade(label="Edición", menu=edicion)

textarea = tk.Text(ventana)
textarea.pack(fill=tk.BOTH, expand=True)

archivo.add_command(label="Nuevo", command = nuevo_archivo)
archivo.add_command(label="Abrir", command = abrir_archivo)
archivo.add_command(label="Guardar", command = guardar_archivo)
archivo.add_command(label="Guardar como", command = guardar_como)

edicion.add_command(label="copiar", command = copiar)
edicion.add_command(label="cortar", command = cortar)
edicion.add_command(label="pegar", command = pegar)

ventana.mainloop()
# Hacer archivo ejecutable >> pyinstaller --onefile notas.py