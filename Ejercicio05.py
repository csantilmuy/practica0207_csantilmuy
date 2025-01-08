# Escribir un programa que abra el fichero con información sobre el PIB per
# cápita de los países de la Unión Europea
# ( https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownload
# Listing?file=data/sdg_08_10.tsv.gz&unzip=true ), pregunte por las iniciales
# de un país y muestre el PIB per cápita de ese país de todos los años
# disponibles.
import csv

def mostrar_pib_pais():
    archivo = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    try:
        iniciales_pais = input("Introduce las iniciales del país (por ejemplo, 'ES' para España): ").upper()
        with open(archivo, 'r', encoding='utf-8') as fichero:
            lector = csv.reader(fichero, delimiter='\t')
            encabezados = next(lector)
            print("Años disponibles:", encabezados[1:])
            for linea in lector:
                if linea[0].startswith(iniciales_pais):
                    print(f"PIB per cápita de {iniciales_pais}:")
                    print(linea[1:])
                    return
            print(f"No se encontraron datos para el país {iniciales_pais}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Descárgalo e intenta nuevamente")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

mostrar_pib_pais()