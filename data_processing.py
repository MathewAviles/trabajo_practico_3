import pandas as pd

def procesar_datos(ruta_archivo):
    """
    Carga, limpia y transforma el dataset de ranking FIFA.
    """
    # Cargar el dataset original
    df = pd.read_csv(ruta_archivo)
    
    # 1. Limpieza: Eliminar filas duplicadas para evitar redundancia
    df = df.drop_duplicates()
    
    # 2. Manejo de nulos: Eliminar registros incompletos
    df = df.dropna()
    
    # 3. Transformación: Asegurar que las columnas tengan el tipo de dato correcto
    df['rank'] = df['rank'].astype(int)
    df['previous_rank'] = df['previous_rank'].astype(int)
    df['points'] = df['points'].astype(float)
    df['previous_points'] = df['previous_points'].astype(float)
    
    # 4. Adaptación: Calcular el cambio de posición (positivo es que subió)
    df['rank_change'] = df['previous_rank'] - df['rank']
    
    # Guardar el dataset procesado para su uso posterior
    ruta_salida = 'fifa_ranking_cleaned.csv'
    df.to_csv(ruta_salida, index=False)
    print(f"Datos procesados exitosamente en: {ruta_salida}")
    return df

if __name__ == "__main__":
    procesar_datos('fifa_ranking_2022-10-06.csv')
