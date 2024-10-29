import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def analizar_puntajes_medicina(archivo):
    # Leer el archivo CSV
    df = pd.read_csv(archivo)
    
    # Filtrar solo los que alcanzaron vacante para algunos análisis
    ingresantes = df[df['Observación'] == 'ALCANZO VACANTE']
    
    # Estadísticas básicas de todos los postulantes
    stats_generales = {
        'Media total': df['Puntaje'].mean(),
        'Mediana total': df['Puntaje'].median(),
        'Moda total': df['Puntaje'].mode().iloc[0],
        'Desviación estándar total': df['Puntaje'].std(),
        'Coeficiente de variación total': (df['Puntaje'].std() / df['Puntaje'].mean()) * 100,
        'Puntaje mínimo total': df['Puntaje'].min(),
        'Puntaje máximo total': df['Puntaje'].max(),
        'Total postulantes': len(df),
        'Total ausentes': len(df[df['Observación'] == 'AUSENTE']),
    }
    
    # Estadísticas de ingresantes
    stats_ingresantes = {
        'Media ingresantes': ingresantes['Puntaje'].mean(),
        'Mediana ingresantes': ingresantes['Puntaje'].median(),
        'Desviación estándar ingresantes': ingresantes['Puntaje'].std(),
        'Coeficiente de variación ingresantes': (ingresantes['Puntaje'].std() / ingresantes['Puntaje'].mean()) * 100,
        'Puntaje mínimo ingreso': ingresantes['Puntaje'].min(),
        'Puntaje máximo ingreso': ingresantes['Puntaje'].max(),
        'Cantidad ingresantes': len(ingresantes),
    }

    # Calcular cuartiles generales
    cuartiles_generales = {
        'Q1 (25%)': df['Puntaje'].quantile(0.25),
        'Q2 (50%)': df['Puntaje'].quantile(0.50),
        'Q3 (75%)': df['Puntaje'].quantile(0.75),
    }

    # Calcular percentiles para todos los postulantes
    percentiles_generales = {f'Percentil {i}': np.percentile(df['Puntaje'].dropna(), i) 
                  for i in [10, 25, 50, 75, 90, 95]}

    # Calcular cuartiles para ingresantes
    cuartiles_ingresantes = {
        'Q1 (25%)': ingresantes['Puntaje'].quantile(0.25),
        'Q2 (50%)': ingresantes['Puntaje'].quantile(0.50),
        'Q3 (75%)': ingresantes['Puntaje'].quantile(0.75),
    }
    
    # Calcular frecuencias de puntajes (por rangos)
    bins = np.linspace(df['Puntaje'].min(), df['Puntaje'].max(), 10)
    frecuencias = pd.cut(df['Puntaje'], bins=bins).value_counts().sort_index()
    
    # Tasa de ingreso
    tasa_ingreso = (len(ingresantes) / len(df)) * 100
    
    # Calcular percentiles relevantes para ingresantes
    percentiles_ingresantes = {f'Percentil {i}': np.percentile(ingresantes['Puntaje'], i) 
                  for i in [10, 25, 50, 75, 90, 95]}
    
    return df, {
        'estadisticas_generales': stats_generales,
        'cuartiles_totales': cuartiles_generales,
        'percentiles_totales': percentiles_generales,
        'estadisticas_ingresantes': stats_ingresantes,
        'cuartiles_ingresantes': cuartiles_ingresantes,
        'frecuencias': frecuencias,
        'tasa_ingreso': tasa_ingreso,
        'percentiles_ingresantes': percentiles_ingresantes
    }

def generar_visualizaciones(df):
    # Configurar el estilo de las gráficas
    plt.style.use('default')
    sns.set_theme()
    
    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Histograma de puntajes
    sns.histplot(data=df, x='Puntaje', ax=axes[0,0], bins=30)
    axes[0,0].set_title('Distribución de Puntajes')
    axes[0,0].set_xlabel('Puntaje')
    axes[0,0].set_ylabel('Frecuencia')
    
    # 2. Boxplot de puntajes por observación
    sns.boxplot(data=df, x='Observación', y='Puntaje', ax=axes[0,1])
    axes[0,1].set_title('Distribución de Puntajes por Resultado')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # 3. Densidad de puntajes
    sns.kdeplot(data=df, x='Puntaje', ax=axes[1,0])
    axes[1,0].set_title('Densidad de Puntajes')
    axes[1,0].set_xlabel('Puntaje')
    
    # 4. Gráfico de violín
    sns.violinplot(data=df, x='Observación', y='Puntaje', ax=axes[1,1])
    axes[1,1].set_title('Distribución detallada por Resultado')
    axes[1,1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    return fig

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        # Leer el archivo y obtener resultados
        archivo = "/home/jsanchez/Projects/applicant-scraper/output/unmsm/MEDICINA HUMANA.csv"
        df, resultados = analizar_puntajes_medicina(archivo)
        
        # Imprimir resultados con formato mejorado
        print("\n================ ANÁLISIS DE PUNTAJES MEDICINA UNMSM ================")
        
        print("\n=== Estadísticas Generales ===")
        for key, value in resultados['estadisticas_generales'].items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
        
        print("\n=== Cuartiles Totales ===")
        for key, value in resultados['cuartiles_totales'].items():
            print(f"{key}: {value:.2f}")

        print("\n=== Percentiles Totales ===")
        for key, value in resultados['percentiles_totales'].items():
            print(f"{key}: {value:.2f}")

        print("\n=== Estadísticas de Ingresantes ===")
        for key, value in resultados['estadisticas_ingresantes'].items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
        
        print("\n=== Cuartiles de Ingresantes ===")
        for key, value in resultados['cuartiles_ingresantes'].items():
            print(f"{key}: {value:.2f}")
        
        print(f"\nTasa de ingreso: {resultados['tasa_ingreso']:.2f}%")
        
        print("\n=== Percentiles de Ingresantes ===")
        for key, value in resultados['percentiles_ingresantes'].items():
            print(f"{key}: {value:.2f}")
            
        # Generar y mostrar visualizaciones
        print("\nGenerando gráficos...")
        fig = generar_visualizaciones(df)
        plt.show()
        
        print("\nAnálisis completado exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except Exception as e:
        print("\n=== ERROR DETALLADO ===")
        print(f"Error en línea: {sys.exc_info()[2].tb_lineno}")
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Mensaje de error: {str(e)}")
        print("\nTraceback completo:")
        print(traceback.format_exc())