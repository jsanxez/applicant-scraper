import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin

def scrape_puntajes_unmsm(url_indice):
    try:
        # Obtener el contenido HTML del índice
        response = requests.get(url_indice)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar la tabla con los enlaces a las escuelas profesionales
        tabla = soup.find('table')
        filas = tabla.find_all('tr')

        # Construir la URL base a partir de la URL del índice
        url_base = url_indice.rsplit('/', 1)[0] + '/'

        # Crear directorio para guardar los archivos CSV
        if not os.path.exists('./output/unmsm'):
            os.makedirs('./output/unmsm')

        # Procesar cada fila de la tabla
        for fila in filas[1:]:  # Omitir la fila de encabezado
            celdas = fila.find_all('td')

            # Obtener el enlace a la escuela profesional
            enlace = celdas[0].find('a')
            url_escuela = urljoin(url_base, enlace.get('href'))
            nombre_escuela = enlace.text.strip()

            # Obtener el contenido HTML de la página de la escuela profesional
            response = requests.get(url_escuela)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontrar la tabla con los puntajes
            tabla = soup.find('table')
            filas = tabla.find_all('tr')

            # Escribir los datos en un archivo CSV
            ruta_archivo_csv = os.path.join('./output/unmsm', f"{nombre_escuela.replace('/', '_')}.csv")
            with open(ruta_archivo_csv, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Escribir el encabezado
                writer.writerow(['Código', 'Apellidos y Nombres', 'Escuela profesional', 'Puntaje', 'Nro. Mérito', 'Observación'])

                # Procesar cada fila de la tabla de puntajes
                for fila in filas[1:]:  # Omitir la fila de encabezado
                    celdas_puntaje = fila.find_all('td')
                    codigo = celdas_puntaje[0].text.strip()
                    nombre = celdas_puntaje[1].text.strip()
                    escuela = celdas_puntaje[2].text.strip()
                    puntaje = celdas_puntaje[3].text.strip()
                    merito = celdas_puntaje[4].text.strip()
                    observacion = celdas_puntaje[5].text.strip()
                    writer.writerow([codigo, nombre, escuela, puntaje, merito, observacion])

            print(f"Datos de {nombre_escuela} guardados en {ruta_archivo_csv}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
url_indice = "https://admision.unmsm.edu.pe/Website20251/A.html"
scrape_puntajes_unmsm(url_indice)