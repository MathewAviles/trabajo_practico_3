# 📊 Proyecto de Análisis de Datos – FIFA Ranking 2022

Este proyecto realiza un análisis completo del dataset de rankings FIFA 2022, incluyendo limpieza de datos, análisis exploratorio (EDA), visualización y un modelo de Machine Learning para identificar patrones entre el ranking y los puntos de cada selección.

---

## 🎯 Objetivo

Analizar el comportamiento de los rankings FIFA y descubrir:

* Relación entre ranking y puntos
* Equipos con mayor crecimiento y caída
* Diferencias entre confederaciones
* Predicción de puntos mediante Machine Learning

---

## 📁 Dataset

Se utilizó un dataset de rankings FIFA que contiene:

* `team`: Nombre del equipo
* `rank`: Ranking actual
* `previous_rank`: Ranking anterior
* `points`: Puntos actuales
* `previous_points`: Puntos anteriores
* `confederation`: Confederación

---

## ⚙️ Procesamiento de Datos

Se realizó limpieza y transformación del dataset:

* Eliminación de duplicados
* Eliminación de valores nulos
* Conversión de tipos de datos
* Creación de nueva variable:

  * `rank_change = previous_rank - rank`

👉 Ejecutar:

```bash
python data_processing.py
```

---

## 📊 Análisis Exploratorio de Datos (EDA)

Se realizó un análisis detallado que permitió identificar:

* Top 10 equipos del mundo
* Equipos que más subieron en ranking
* Equipos que más bajaron
* Promedio de puntos por ranking
* Verificación de consistencia de datos

👉 Ejecutar:

```bash
python eda_analysis.py
```

---

## 📈 Visualización de Datos

Se generaron gráficos informativos utilizando **matplotlib**:

* Top 10 equipos por puntos
* Equipos que más subieron
* Equipos que más bajaron

👉 Ejecutar:

```bash
python visualizations.py
```

---

## 🤖 Machine Learning

Se implementó un modelo de regresión lineal para predecir los puntos en función del ranking.

* Modelo utilizado: `LinearRegression`
* Variable independiente: `rank`
* Variable dependiente: `points`
* Métrica de evaluación: MAE (Error Medio Absoluto)

### 📌 Resultados del modelo

* Error promedio aproximado: **19 puntos**
* Se confirma una relación lineal entre ranking y puntos

👉 Ejecutar:

```bash
python model.py
```

---

## 📊 Insights del Análisis

* Existe una relación inversa entre ranking y puntos
* Los equipos mejor posicionados tienen mayor puntaje
* Se identificaron selecciones con crecimiento significativo
* El ranking refleja de forma consistente el rendimiento de los equipos
* El modelo de Machine Learning confirma la tendencia observada

---

## 🚀 Ejecución del Proyecto

### 1️⃣ Instalar dependencias

```bash
pip install pandas matplotlib scikit-learn plotly
```

### 2️⃣ Ejecutar en orden

```bash
python data_processing.py
python eda_analysis.py
python visualizations.py
python model.py
```

---

## 📚 Tecnologías utilizadas

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## 👥 Autor

* Jorge Brito

---
## 🔄 Trabajo Colaborativo

El proyecto se desarrolló utilizando GitHub mediante el uso de ramas (branches) y Pull Requests, permitiendo integrar el trabajo de cada miembro del equipo de forma organizada y controlada.
## 📊 Valor del Proyecto

Este análisis permite comprender el comportamiento del ranking FIFA y demuestra cómo los datos pueden ser utilizados para generar conocimiento útil y predicciones en el ámbito deportivo.

## 📌 Conclusión

Este proyecto demuestra cómo el análisis de datos permite identificar patrones relevantes en el ranking FIFA. Además, evidencia que técnicas de Machine Learning pueden ser utilizadas para predecir el comportamiento de variables deportivas, aportando valor analítico y predictivo al estudio.

---
