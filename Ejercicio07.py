# El fichero calificaciones.csv contiene las calificaciones de un curso.
# Durante el curso se realizan dos exámenes parciales de teoría y un examen
# de prácticas. Los alumnos que tengan menos de 4 en alguno de estos exámenes
# pueden repetirlo al final del curso (convocatoria ordinaria). Escribir un
# programa que contenga las siguientes funciones:
# - Una función que reciba el fichero de calificaciones y devuelva una lista
# de diccionarios, donde cada diccionario contiene la información de los
# exámenes y la asistencia de un alumno. La lista tiene que estar ordenada
# por apellidos.
# - Una función que reciba una lista de diccionarios como la que devuelve la
# función anterior y añada a cada diccionario un nuevo par con la nota final
# del curso. El peso de cada parcial de teoría en la nota final es de un 30%
# mientras que el peso del examen de prácticas es de un 40%.
# - Una función que reciba una lista de diccionarios como la que devuelve la
# función anterior y devuelva dos listas, una con los alumnos aprobados y otra
# con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que
# ser mayor o igual que el 75%, la nota de los exámenes parciales y de
# prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

import csv

def leer_calificaciones(archivo):
    alumnos = []
    with open(archivo, mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            alumno = {
                "apellido": fila["apellido"],
                "teoria1": float(fila["teoria1"]),
                "teoria2": float(fila["teoria2"]),
                "practicas": float(fila["practicas"]),
                "asistencia": float(fila["asistencia"])
            }
            alumnos.append(alumno)
    alumnos.sort(key=lambda x: x["apellido"])
    return alumnos

def calcular_notas_finales(alumnos):
    for alumno in alumnos:
        nota_final = (alumno["teoria1"] * 0.3 +
                      alumno["teoria2"] * 0.3 +
                      alumno["practicas"] * 0.4)
        alumno["nota_final"] = nota_final
    return alumnos

def clasificar_alumnos(alumnos):
    aprobados = []
    suspensos = []
    for alumno in alumnos:
        if (alumno["asistencia"] >= 75 and
                alumno["teoria1"] >= 4 and
                alumno["teoria2"] >= 4 and
                alumno["practicas"] >= 4 and
                alumno["nota_final"] >= 5):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos

archivo = "calificaciones.csv"
alumnos = leer_calificaciones(archivo)
alumnos = calcular_notas_finales(alumnos)
aprobados, suspensos = clasificar_alumnos(alumnos)

print("Alumnos Aprobados:")
for alumno in aprobados:
    print(alumno)

print("\nAlumnos Suspensos:")
for alumno in suspensos:
    print(alumno)