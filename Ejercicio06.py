# Escribir un programa para gestionar un listín telefónico con los nombres y
# los teléfonos de los clientes de una empresa. El programa debe  incorporar
# funciones para crear el fichero con el listín si no existe, para consultar
# el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar
# el teléfono de un cliente. El listín debe estar guardado en el fichero de
# texto listin.txt donde el nombre del cliente y su teléfono deben aparecer
# separados por comas y cada cliente en una línea distinta.

def crear_listin(nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        pass

def consultar_listin(nombre_archivo, cliente):
    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:
                nombre, telefono = linea.strip().split(",")
                if nombre == cliente:
                    return telefono
    except FileNotFoundError:
        print("El archivo no existe")
    return None

def anadir_cliente(nombre_archivo, cliente, telefono):
    with open(nombre_archivo, 'a') as f:
        f.write(f"{cliente},{telefono}\n")

def eliminar_cliente(nombre_archivo, cliente):
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.readlines()
        with open(nombre_archivo, 'w') as f:
            for linea in lineas:
                if not linea.startswith(cliente + ","):
                    f.write(linea)
    except FileNotFoundError:
        print("El archivo no existe")

nombre_archivo = "listin.txt"

while True:
    print("\nGestión de Listín Telefónico")
    print("1. Crear listín")
    print("2. Consultar teléfono")
    print("3. Añadir cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_listin(nombre_archivo)
        print("Listín creado")
    elif opcion == "2":
        cliente = input("Introduce el nombre del cliente: ")
        telefono = consultar_listin(nombre_archivo, cliente)
        if telefono:
            print(f"Teléfono de {cliente}: {telefono}")
        else:
            print("Cliente no encontrado")
    elif opcion == "3":
        cliente = input("Introduce el nombre del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        anadir_cliente(nombre_archivo, cliente, telefono)
        print("Cliente añadido")
    elif opcion == "4":
        cliente = input("Introduce el nombre del cliente: ")
        eliminar_cliente(nombre_archivo, cliente)
        print("Cliente eliminado")
    elif opcion == "5":
        break
    else:
        print("Opción no válida")