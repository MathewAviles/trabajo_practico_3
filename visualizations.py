import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

def guardar_grafico_segmentado(fig, nombre_base, titulo):
    """
    Exporta un gráfico de Plotly en un archivo HTML limpio y un archivo JS con los datos.
    """
    # Extraer los datos del gráfico a JSON
    grafico_json = pio.to_json(fig)
    
    # Crear el archivo JS
    js_content = f"const data_{nombre_base} = {grafico_json};\n"
    js_content += f"Plotly.newPlot('{nombre_base}', data_{nombre_base}.data, data_{nombre_base}.layout);"
    
    with open(f"static/js/{nombre_base}.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    # Crear el archivo HTML
    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{titulo}</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div id="{nombre_base}" style="width:100%;height:100vh;"></div>
    <script src="js/{nombre_base}.js"></script>
</body>
</html>
"""
    with open(f"static/{nombre_base}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def crear_visualizaciones(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    
    # Asegurar que existan las carpetas de salida
    import os
    os.makedirs('static/js', exist_ok=True)
    
    # 1. Mapa Coroplético Global
    fig_map = px.choropleth(df, 
                            locations='team_code', 
                            color='points', 
                            hover_name='team',
                            title='Mapa Global de Puntos FIFA (Octubre 2022)',
                            color_continuous_scale=px.colors.sequential.Plasma)
    guardar_grafico_segmentado(fig_map, 'mapa_global', 'Ranking FIFA - Mapa Mundial')
    
    # 2. Distribución de Puntos por Asociación
    fig_box = px.box(df, 
                     x='association', 
                     y='points', 
                     color='association',
                     title='Distribución de Puntos por Confederación')
    guardar_grafico_segmentado(fig_box, 'distribucion_asoc', 'Distribución por Confederación')
    
    # 3. Top 10 Equipos
    top_10 = df.nsmallest(10, 'rank')
    fig_bar = px.bar(top_10, 
                     x='team', 
                     y='points', 
                     text='rank',
                     title='Top 10 Selecciones Mundiales',
                     color='points')
    guardar_grafico_segmentado(fig_bar, 'top_10', 'Top 10 Selecciones')
    
    print("Visualizaciones segmentadas generadas en la carpeta 'static/'")

if __name__ == '__main__':
    crear_visualizaciones('fifa_ranking_cleaned.csv')
