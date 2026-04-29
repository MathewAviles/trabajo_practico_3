# Proyecto de Análisis de Datos FIFA 2022 - FastAPI

Este proyecto consiste en una API construida con FastAPI para analizar el dataset de rankings de la FIFA de 2022. Todo el código fuente está debidamente comentado en español.

## Estructura del Proyecto

- `data_processing.py`: Script para la limpieza y transformación de datos.
- `eda_analysis.py`: Análisis exploratorio de datos para identificar patrones y anomalías.
- `visualizations.py`: Generador de gráficos interactivos usando Plotly.
- `static/`: Carpeta que contiene las visualizaciones segmentadas (HTML y JS por separado).
- `fifa_ranking_cleaned.csv`: Dataset procesado listo para el análisis.
Este proyecto es una plataforma de análisis de datos basada en el ranking mundial de la FIFA de octubre de 2022. Utiliza **FastAPI** para el backend y **Plotly** para visualizaciones interactivas de alto impacto.

**Autor de los cambios:** Mathew Avilés

## 📂 Estructura del Proyecto

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
- `data_processing.py`: Script de limpieza y transformación de datos (Python).
- `eda_analysis.py`: Análisis exploratorio para identificar patrones y anomalías.
- `visualizations.py`: Generador de gráficos interactivos (Mapa, BoxPlot, Barras).
- `static/`: Contiene los archivos HTML finales listos para ser visualizados.
- `fifa_ranking_cleaned.csv`: Dataset optimizado tras el procesamiento.
- `venv/`: Entorno virtual con las dependencias del proyecto.

## 🚀 Guía Paso a Paso

### 1. Configuración del Entorno
Se creó un entorno virtual de Python y se instalaron las librerías necesarias para el análisis de datos:
- `pandas`: Para el manejo de estructuras de datos.
- `plotly`: Para la generación de gráficos interactivos.
- `fastapi` y `uvicorn`: Para la futura implementación de la API.

### 2. Procesamiento de Datos (Limpieza)
El dataset original fue sometido a un proceso de curación:
- Eliminación de duplicados y valores nulos.
- Cálculo de la métrica **Cambio de Ranking** (diferencia con el mes anterior).
- Normalización de tipos de datos numéricos.
- **Cómo ejecutar:** `python data_processing.py`

### 3. Análisis Exploratorio (EDA)
Se realizó un estudio detallado que reveló:
- **Liderazgo Regional:** CONMEBOL posee el promedio de puntos más alto por confederación.
- **Progreso:** Identificación de equipos con mayor ascenso en la tabla.
- **Consistencia:** Verificación de que no existen anomalías en los puntajes.
- **Cómo ejecutar:** `python eda_analysis.py`

### 4. Visualización de Datos (Plotly)
Se generaron tres tableros interactivos con etiquetas totalmente en **español**:
- **Mapa Global:** Distribución de puntos en el mapa mundial con escala de colores.
- **Distribución por Confederación:** Comparativa de la dispersión de puntos por región.
- **Top 10 Mundial:** Gráfico de barras con las mejores selecciones actuales.
- **Cómo ejecutar:** `python visualizations.py`

## 📊 Cómo ver los resultados

Para ver las gráficas interactivas, simplemente abre los archivos dentro de la carpeta `static/` con tu navegador favorito (Chrome, Edge, Firefox):

1.  **Mapa Mundial:** `static/mapa_global.html`
2.  **Análisis de Confederaciones:** `static/distribucion_asoc.html`
3.  **Ranking Top 10:** `static/top_10.html`

*Nota: Al pasar el cursor sobre los gráficos, podrás ver detalles específicos como el nombre del Equipo y sus Puntos exactos.*
