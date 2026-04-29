# Proyecto de Análisis de Datos FIFA 2022 - FastAPI

Este proyecto consiste en una API construida con FastAPI para analizar el dataset de rankings de la FIFA de 2022.

## Pasos realizados

1. **Configuración del entorno:**
   - Creación de la rama `mathew_dev`.
   - Configuración del entorno virtual (`venv`).

2. **Procesamiento de datos:**
   - Se analizó el dataset original `fifa_ranking_2022-10-06.csv`.
   - Se creó el script `data_processing.py` para la limpieza y transformación.
   - **Limpieza:** Se eliminaron duplicados y valores nulos.
   - **Transformación:** Se aseguraron los tipos de datos numéricos.
   - **Adaptación:** Se creó la columna `rank_change` para calcular la diferencia de posiciones respecto al mes anterior.
   - El resultado se guardó en `fifa_ranking_cleaned.csv`.

3. **Análisis Exploratorio de Datos (EDA):**
   - Se implementó el script `eda_analysis.py`.
   - **Estadísticas:** El promedio global de puntos es de ~1220 pts.
   - **Patrones por Asociación:** CONMEBOL lidera con el promedio de puntos más alto (1554 pts), seguida por UEFA (1380 pts).
   - **Dinámica de Ranking:** Equipos como Escocia y Azerbaiyán mostraron el mayor crecimiento (+5 posiciones).
   - **Anomalías:** No se encontraron variaciones de puntos extremas, lo que sugiere consistencia en los datos.

4. **Visualización de datos:**
   - Se utilizó la librería **Plotly** para generar gráficos interactivos.
   - **Mapa Global:** Se creó un mapa coroplético (`viz_mapa_global.html`) que muestra la intensidad de puntos por país.
   - **Distribución por Confederación:** Un gráfico de caja (`viz_distribucion_asociacion.html`) para comparar el rendimiento entre confederaciones.
   - **Top 10:** Gráfico de barras (`viz_top_10_equipos.html`) con las mejores selecciones según el ranking.


