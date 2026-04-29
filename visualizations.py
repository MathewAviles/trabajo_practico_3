import pandas as pd
import plotly.express as px
import os

def crear_visualizaciones(ruta_archivo):
    """
    Genera visualizaciones interactivas de Plotly con etiquetas en español.
    """
    # Cargar los datos procesados
    df = pd.read_csv(ruta_archivo)
    
    # Asegurar que el directorio de salida exista
    os.makedirs('static', exist_ok=True)
    
    # Diccionario de traducción para las etiquetas
    traducciones = {
        'team': 'Equipo',
        'points': 'Puntos',
        'association': 'Confederación',
        'rank': 'Ranking',
        'previous_rank': 'Ranking Anterior',
        'rank_change': 'Cambio de Ranking'
    }
    
    # 1. Mapa Coroplético Global
    fig_map = px.choropleth(df, 
                            locations='team', 
                            locationmode='country names',
                            color='points', 
                            hover_name='team',
                            hover_data={'team': False, 'points': True}, # Personalizar tooltip
                            title='<b>Distribución Global de Puntos FIFA (Octubre 2022)</b>',
                            labels=traducciones,
                            color_continuous_scale='Viridis')
    
    fig_map.update_layout(
        geo=dict(showframe=False, showcoastlines=True, projection_type='natural earth'),
        margin=dict(l=0, r=0, t=50, b=0),
        coloraxis_colorbar_title="Puntos"
    )
    fig_map.write_html("static/mapa_global.html", include_plotlyjs="cdn")
    
    # 2. Box Plot de Confederaciones
    fig_box = px.box(df, 
                     x='association', 
                     y='points', 
                     color='association',
                     title='<b>Dispersión de Puntos por Confederación</b>',
                     labels=traducciones,
                     points='all')
    
    fig_box.update_layout(showlegend=False)
    fig_box.write_html("static/distribucion_asoc.html", include_plotlyjs="cdn")
    
    # 3. Top 10 de Selecciones
    top_10 = df.nsmallest(10, 'rank')
    fig_bar = px.bar(top_10, 
                     x='team', 
                     y='points', 
                     text='points',
                     title='<b>Top 10 Selecciones Nacionales</b>',
                     labels=traducciones,
                     color='points',
                     color_continuous_scale='Blues')
    
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(coloraxis_showscale=False)
    fig_bar.write_html("static/top_10.html", include_plotlyjs="cdn")
    
    print("¡Visualizaciones actualizadas con etiquetas en español!")

if __name__ == '__main__':
    crear_visualizaciones('fifa_ranking_cleaned.csv')
