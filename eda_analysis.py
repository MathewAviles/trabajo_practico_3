import pandas as pd

def ejecutar_eda(ruta_archivo):
    """
    Realiza un Análisis Exploratorio de Datos detallado.
    """
    df = pd.read_csv(ruta_archivo)
    
    print("--- Análisis Exploratorio de Datos (FIFA 2022) ---")
    
    # 1. Resumen estadístico de los puntos
    print("\n[1] Estadísticas descriptivas de los puntos:")
    print(df['points'].describe())
    
    # 2. Análisis de rendimiento por confederación (Patrones regionales)
    print("\n[2] Promedio de puntos por Asociación (Confederación):")
    stats_asoc = df.groupby('association')['points'].mean().sort_values(ascending=False)
    print(stats_asoc)
    
    # 3. Identificación de equipos con mayor progreso
    print("\n[3] Top 5 equipos con mayor ascenso en el ranking:")
    print(df.nlargest(5, 'rank_change')[['team', 'rank', 'previous_rank', 'rank_change']])
    
    # 4. Detección de anomalías o cambios significativos de puntaje
    print("\n[4] Detección de cambios bruscos de puntos (>20 pts):")
    df['diferencia_puntos'] = (df['points'] - df['previous_points']).abs()
    anomalias = df[df['diferencia_puntos'] > 20]
    if not anomalias.empty:
        print(anomalias[['team', 'points', 'previous_points', 'diferencia_puntos']])
    else:
        print("No se detectaron anomalías significativas.")

if __name__ == "__main__":
    ejecutar_eda('fifa_ranking_cleaned.csv')
