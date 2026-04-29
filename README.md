# Proyecto de Análisis de Datos FIFA 2022 - FastAPI

Este proyecto es una plataforma de análisis de datos basada en el ranking mundial de la FIFA de octubre de 2022. Utiliza **FastAPI** para el backend y **Plotly** para visualizaciones interactivas de alto impacto.

**Autor de los cambios:** Mathew Avilés

## 📂 Estructura del Proyecto

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
