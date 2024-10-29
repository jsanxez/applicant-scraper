from bs4 import BeautifulSoup
import csv
import os

def procesar_archivo_html(ruta_archivo_html, ruta_archivo_csv='resultados.csv'):
    """
    Lee un archivo HTML y extrae los datos de la tabla a un archivo CSV.
    
    Args:
        ruta_archivo_html (str): Ruta al archivo HTML
        ruta_archivo_csv (str): Ruta donde se guardará el archivo CSV
    """
    try:
        # Verificar que el archivo HTML existe
        if not os.path.exists(ruta_archivo_html):
            raise FileNotFoundError(f"El archivo {ruta_archivo_html} no existe")
        
        # Leer el archivo HTML
        with open(ruta_archivo_html, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Encontrar todas las filas de la tabla
        rows = soup.find_all('tr')
        
        if not rows:
            raise ValueError("No se encontraron filas en la tabla")
        
        # Abrir el archivo CSV para escribir
        with open(ruta_archivo_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Escribir el encabezado
            writer.writerow(['Código', 'Apellidos y Nombres', 'Escuela Profesional', 
                           'Puntaje', 'Mérito', 'Observación'])
            
            # Contador para filas procesadas
            filas_procesadas = 0
            
            # Procesar cada fila
            for row in rows:
                cells = row.find_all('td')
                
                if len(cells) == 6:  # Verificar que la fila tiene 6 columnas
                    # Extraer el texto de cada celda
                    datos_fila = [cell.text.strip() for cell in cells]
                    
                    # Escribir la fila en el CSV
                    writer.writerow(datos_fila)
                    filas_procesadas += 1
        
        print(f"Proceso completado exitosamente:")
        print(f"- Se procesaron {filas_procesadas} filas")
        print(f"- El archivo CSV se guardó en: {os.path.abspath(ruta_archivo_csv)}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Uso del script
if __name__ == "__main__":
    # Reemplazar 'archivo.html' con el nombre de tu archivo HTML
    procesar_archivo_html('./rsrc/medicina.html', './output/medicina.csv')