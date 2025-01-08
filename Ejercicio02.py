# Escribir una función que pida un número entero entre 1 y 10, lea el fichero
# tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número
# introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar
# un mensaje por pantalla informando de ello.
def leer_tabla_multiplicar():
    n = int(input("Escribe un número entre 1 y 10: "))
    if 1 <= n <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, 'r') as fichero:
                print(f"Contenido de {nombre_fichero}:")
                print(fichero.read())
        except FileNotFoundError:
            print(f"El archivo {nombre_fichero} no existe")
    else:
        print("El número debe estar entre 1 y 10")

leer_tabla_multiplicar()