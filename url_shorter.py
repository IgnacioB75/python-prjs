''' Acortador URL con Python
    + Bibliotecas: streamlit & pyshorteners
    
    * Para iniciarlo escribir en el terminal >> streamlit run url_shorter.py
    * Para detenerlo desde el terminal: Ctrl+C 
'''

import pyshorteners
import streamlit as st

def shorten_url(url): # Función acortadora de URLs
    s = pyshorteners.Shortener() 
    shortened_url = s.tinyurl.short(url) # Método para acortarlo
    return shortened_url

# Página web
st.set_page_config(page_title="URL shortener", page_icon="✏", layout="centered") # Titulo e icono de la página y diseño centrado
st.title("URL shorter") # Título de la páquina
url = st.text_input("Enter the URL") # Texto de la entrada
if st.button("Generate new URL"): # Botón de generar URL
    st.write("URL shortened: ", shorten_url(url)) # Mensaje con el URL acortado