# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero
# tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla
# la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por
# pantalla informando de ello.
def leer_linea_tabla_multiplicar():
    n = int(input("Escribe el número de la tabla (entre 1 y 10): "))
    m = int(input("Escribe la línea que quieres leer (entre 1 y 10): "))
    if 1 <= n <= 10 and 1 <= m <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, 'r') as fichero:
                lineas = fichero.readlines()
                print(f"Línea {m} de la tabla del {n}: {lineas[m - 1].strip()}")
        except FileNotFoundError:
            print(f"El archivo {nombre_fichero} no existe")
        except IndexError:
            print("La línea solicitada no existe en el archivo")
    else:
        print("Ambos números deben estar entre 1 y 10")

leer_linea_tabla_multiplicar()