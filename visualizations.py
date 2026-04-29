import pandas as pd
import plotly.express as px
import plotly.io as pio

def create_visualizations(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Mapa Coroplético Global
    fig_map = px.choropleth(df, 
                            locations='team_code', 
                            color='points', 
                            hover_name='team',
                            title='Mapa Global de Puntos FIFA (Octubre 2022)',
                            color_continuous_scale=px.colors.sequential.Plasma)
    fig_map.write_html('viz_mapa_global.html')
    
    # 2. Distribución de Puntos por Asociación (Box Plot)
    fig_box = px.box(df, 
                     x='association', 
                     y='points', 
                     color='association',
                     title='Distribución de Puntos por Confederación',
                     points='all')
    fig_box.write_html('viz_distribucion_asociacion.html')
    
    # 3. Top 10 Equipos (Bar Chart)
    top_10 = df.nsmallest(10, 'rank')
    fig_bar = px.bar(top_10, 
                     x='team', 
                     y='points', 
                     text='rank',
                     title='Top 10 Selecciones Mundiales',
                     color='points',
                     labels={'team': 'Equipo', 'points': 'Puntos'})
    fig_bar.write_html('viz_top_10_equipos.html')
    
    print('Visualizaciones generadas: viz_mapa_global.html, viz_distribucion_asociacion.html, viz_top_10_equipos.html')

if __name__ == '__main__':
    create_visualizations('fifa_ranking_cleaned.csv')
