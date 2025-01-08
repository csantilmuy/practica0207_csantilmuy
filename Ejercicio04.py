# Escribir un programa que acceda al fichero de internet mediante la url
# indicada y muestre por pantalla el número de palabras que contiene.
# http://textfiles.com/adventure/aencounter.txt

import urllib.request

def contar_palabras_url():
    url = "http://textfiles.com/adventure/aencounter.txt"
    try:
        with urllib.request.urlopen(url) as respuesta:
            contenido = respuesta.read().decode('utf-8')
            palabras = contenido.split()
            print(f"El archivo contiene {len(palabras)} palabras")
    except Exception as e:
        print(f"Error al acceder a la URL: {e}")

contar_palabras_url()