import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input, register_page
import plotly.express as px
import plotly.graph_objects as go

# Load Excel
data_hoja3 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_by_sector_and_countr')

data_3 = data_hoja3.melt(
    id_vars=['Sector', 'ISOcode', 'Country'],  
    var_name='Year',                 
    value_name='CO2 Emissions'       
)

# Agrupar por 'Sector' y 'Year' y calcular la media de 'CO2 Emissions'
grouped_data_sectors = data_3.groupby(['Sector', 'Year'])['CO2 Emissions'].mean().reset_index()

# Convertir la columna 'Year' a tipo numérico
data_3['Year'] = pd.to_numeric(data_3['Year'])

# Crear una nueva columna para las décadas
data_3['Decade'] = (data_3['Year'] // 10) * 10

# Agrupar por 'Sector', 'Decade' y 'Country' y calcular la media de 'CO2 Emissions'
grouped_data_decades = data_3.groupby(['Sector', 'Decade', 'Country'])['CO2 Emissions'].mean().reset_index()

register_page(__name__, name='sectors', path='/sectors')

layout = html.Div([
    html.Div([
        html.Div([
            dcc.Checklist(
                id='checklist-sectors',
                options=[{'label': sector, 'value': sector} for sector in grouped_data_sectors['Sector'].unique()] + [{'label': 'All Sectors', 'value': 'All Sectors'}],
                value=['All Sectors'],
                labelStyle={'display': 'block'}
            ),
            dcc.Graph(id='line-chart')
        ], style={'width': '60%', 'display': 'inline-block', 'vertical-align': 'top'}),

        html.Div([
            dcc.Dropdown(
                id='dropdown-year',
                options=[{'label': str(year), 'value': year} for year in grouped_data_sectors['Year'].unique()],
                value=grouped_data_sectors['Year'].min(),
                placeholder="Select a year"
            ),
            dcc.Graph(id='donut-chart')
        ], style={'width': '33%', 'display': 'inline-block', 'vertical-align': 'top'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),
])

@callback(
    Output('donut-chart', 'figure'),
    [Input('dropdown-year', 'value')]
)
def update_donut_chart(selected_year):
    filtered_data = grouped_data_sectors[grouped_data_sectors['Year'] == selected_year]
    
    fig = go.Figure(data=[go.Pie(
        labels=filtered_data['Sector'],
        values=filtered_data['CO2 Emissions'],
        hole=0.4,  # Crear efecto de dona
        title=f'CO2 Emissions'  # Título dentro del gráfico
    )])

    # Título encima del gráfico
    fig.update_layout(
        title_text=f"CO2 Emissions Distribution by Sector in {selected_year}",
        title_x=0.5,  # Centrar el título
        title_y=0.95  # Asegurarse de que esté por encima del gráfico
    )
    
    return fig
