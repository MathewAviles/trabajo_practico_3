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
