import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

def guardar_grafico_segmentado(fig, nombre_base, titulo):
    """
    Exporta un gráfico de Plotly de forma segmentada (HTML + JS) de manera robusta.
    """
    # Asegurar que existan las carpetas
    os.makedirs('static/js', exist_ok=True)
    
    # Obtener el JSON de la figura completa (incluye data y layout)
    fig_json = pio.to_json(fig)
    
    # Crear el archivo JS: Asignamos el JSON a una constante y llamamos a Plotly.newPlot
    # Usamos la figura completa directamente
    js_content = f"const fig_{nombre_base} = {fig_json};\n"
    js_content += f"Plotly.newPlot('{nombre_base}', fig_{nombre_base});"
    
    with open(f"static/js/{nombre_base}.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    # Crear el archivo HTML con estilo para asegurar visibilidad
    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <!-- Cargamos Plotly desde su CDN oficial -->
    <script src="https://cdn.plot.ly/plotly-2.24.1.min.js"></script>
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; overflow: hidden; }}
        #{nombre_base} {{ width: 100vw; height: 100vh; }}
    </style>
</head>
<body>
    <div id="{nombre_base}"></div>
    <!-- Cargamos los datos y la lógica del gráfico -->
    <script src="js/{nombre_base}.js"></script>
</body>
</html>
"""
    with open(f"static/{nombre_base}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def crear_visualizaciones(ruta_archivo):
    # Cargar datos limpios
    df = pd.read_csv(ruta_archivo)
    
    # 1. Mapa Coroplético Global (Corregido para máxima compatibilidad)
    fig_map = px.choropleth(df, 
                            locations='team_code', 
                            color='points', 
                            hover_name='team',
                            title='Ranking FIFA 2022 - Distribución Global de Puntos',
                            color_continuous_scale='Viridis',
                            projection='natural earth') # Añadimos proyección explícita
    
    fig_map.update_layout(
        margin={"r":0,"t":40,"l":0,"b":0},
        paper_bgcolor="white"
    )
    guardar_grafico_segmentado(fig_map, 'mapa_global', 'Mapa Mundial FIFA')
    
    # 2. Distribución de Puntos por Confederación
    fig_box = px.box(df, 
                     x='association', 
                     y='points', 
                     color='association',
                     title='Comparativa de Puntos por Confederación',
                     points='all')
    guardar_grafico_segmentado(fig_box, 'distribucion_asoc', 'Puntos por Confederación')
    
    # 3. Top 10 Equipos
    top_10 = df.nsmallest(10, 'rank')
    fig_bar = px.bar(top_10, 
                     x='team', 
                     y='points', 
                     text='points',
                     title='Top 10 Selecciones Nacionales',
                     color='points',
                     color_continuous_scale='Blues')
    
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(xaxis_title="Selección", yaxis_title="Puntos Totales")
    
    guardar_grafico_segmentado(fig_bar, 'top_10', 'Top 10 Mundial')
    
    print("¡Visualizaciones corregidas y generadas exitosamente en 'static/'!")

if __name__ == '__main__':
    crear_visualizaciones('fifa_ranking_cleaned.csv')
