# Proyecto de Análisis de Datos FIFA 2022 - FastAPI

Este proyecto consiste en una API construida con FastAPI para analizar el dataset de rankings de la FIFA de 2022. Todo el código fuente está debidamente comentado en español.

## Estructura del Proyecto

- `data_processing.py`: Script para la limpieza y transformación de datos.
- `eda_analysis.py`: Análisis exploratorio de datos para identificar patrones y anomalías.
- `visualizations.py`: Generador de gráficos interactivos usando Plotly.
- `static/`: Carpeta que contiene las visualizaciones segmentadas (HTML y JS por separado).
- `fifa_ranking_cleaned.csv`: Dataset procesado listo para el análisis.

## Pasos realizados

1. **Configuración del entorno:**
   - Creación de la rama `mathew_dev`.
   - Configuración del entorno virtual (`venv`).

2. **Procesamiento de datos:**
   - **Limpieza:** Eliminación de duplicados y valores nulos.
   - **Transformación:** Conversión de tipos de datos y creación de la métrica `rank_change`.
   - El código ha sido comentado íntegramente en español para facilitar su mantenimiento.

3. **Análisis Exploratorio de Datos (EDA):**
   - Identificación de promedios por confederación (CONMEBOL liderando en puntaje).
   - Análisis de equipos con mayor crecimiento (+5 posiciones para Escocia y Azerbaiyán).
   - Validación de consistencia en los datos (sin anomalías extremas).

4. **Visualización de datos (Segmentada):**
   - Se implementó una arquitectura limpia separando el **HTML** del **JavaScript**.
   - Los archivos se encuentran en la carpeta `static/`.
   - Se generaron mapas globales, diagramas de caja por confederación y rankings de los 10 mejores equipos.
