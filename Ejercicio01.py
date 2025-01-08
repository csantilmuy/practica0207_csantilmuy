# Escribir una función que pida un número entero entre 1 y 10 y guarde en un
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
# donde n es el número introducido
def guardar_tabla_multiplicar():
    n = int(input("Escribe un número entre 1 y 10: "))
    if 1 <= n <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        with open(nombre_fichero, 'w') as fichero:
            for i in range(1, 11):
                fichero.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}")
    else:
        print("El número debe estar entre 1 y 10")

guardar_tabla_multiplicar()