import pandas as pd

def process_data(file_path):
    # Cargar el dataset
    df = pd.read_csv(file_path)
    
    # 1. Limpieza: Eliminar posibles duplicados
    df = df.drop_duplicates()
    
    # 2. Manejo de nulos (si los hay)
    df = df.dropna()
    
    # 3. Transformación: Asegurar tipos de datos
    df['rank'] = df['rank'].astype(int)
    df['previous_rank'] = df['previous_rank'].astype(int)
    df['points'] = df['points'].astype(float)
    df['previous_points'] = df['previous_points'].astype(float)
    
    # 4. Adaptación: Crear columna de cambio de posición
    df['rank_change'] = df['previous_rank'] - df['rank']
    
    # Guardar el dataset limpio
    output_path = 'fifa_ranking_cleaned.csv'
    df.to_csv(output_path, index=False)
    print(f"Datos procesados y guardados en {output_path}")
    return df

if __name__ == "__main__":
    process_data('fifa_ranking_2022-10-06.csv')
