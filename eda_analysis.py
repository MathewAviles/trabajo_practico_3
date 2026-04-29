import pandas as pd

def run_eda(file_path):
    df = pd.read_csv(file_path)
    
    print("--- Análisis Exploratorio de Datos (FIFA 2022) ---")
    
    # 1. Estadísticas Generales
    print("\n[1] Estadísticas descriptivas de los puntos:")
    print(df['points'].describe())
    
    # 2. Análisis por Asociación (Patrones)
    print("\n[2] Promedio de puntos por Asociación (Confederación):")
    assoc_stats = df.groupby('association')['points'].mean().sort_values(ascending=False)
    print(assoc_stats)
    
    # 3. Equipos con mayor progreso (Patrones de cambio)
    print("\n[3] Top 5 equipos que más subieron en el ranking:")
    print(df.nlargest(5, 'rank_change')[['team', 'rank', 'previous_rank', 'rank_change']])
    
    # 4. Detección de Anomalías
    # Buscamos cambios bruscos de puntos (más de 50 puntos de diferencia)
    print("\n[4] Detección de cambios bruscos de puntos (Posibles anomalías o hitos):")
    df['point_diff'] = (df['points'] - df['previous_points']).abs()
    anomalies = df[df['point_diff'] > 20] # 20 puntos es un cambio significativo en un solo periodo
    if not anomalies.empty:
        print(anomalies[['team', 'points', 'previous_points', 'point_diff']])
    else:
        print("No se detectaron cambios extremos de puntaje (>20 pts).")

    # 5. Distribución de equipos por asociación
    print("\n[5] Cantidad de equipos por Asociación:")
    print(df['association'].value_counts())

if __name__ == "__main__":
    run_eda('fifa_ranking_cleaned.csv')
