import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input, register_page
import plotly.express as px
from config import app_config

# Cargar datos globalmente
archivo_excel = pd.ExcelFile('CO2.xlsx')
data_hoja1 = pd.read_excel(archivo_excel, sheet_name='fossil_CO2_totals_by_country')

# Convertir los datos a formato largo
data_h1 = data_hoja1.melt(
    id_vars=['ISOcode', 'Country'],
    var_name='Year',
    value_name='CO2 Emissions'
)

# Establecer configuraciones de países y años desde la configuración
countries = app_config['Country']
years = app_config['Year']

# Register page en lugar de app
register_page(__name__, name='page2', path='/page2')

layout = html.Div([
    dcc.Dropdown(
        id='dropdown-year',
        options=[{'label': year, 'value': year} for year in app_config['Year']],
        placeholder="Select a year"
    ),
    dcc.Graph(id='graph-year'),
], style={'width': '48%', 'display': 'inline-block'})

# Callback para actualizar el gráfico por año
@callback(
    Output('graph-year', 'figure'),
    Input('dropdown-year', 'value')
)
def update_graph_page2(selected_year):
    if not selected_year:
        return {}  # Retorna un gráfico vacío si no se selecciona un año
    
    # Filtrar los datos para el año seleccionado
    df_year = data_h1[data_h1['Year'] == selected_year]
    
    # Crear gráfico de barras
    fig_year = px.bar(
        df_year, x='Country', y='CO2 Emissions',
        title=f'CO2 emissions in {selected_year} per country',
        labels={'CO2 Emissions': 'CO2 emissions (tons)'}
    )
    
    return fig_year
