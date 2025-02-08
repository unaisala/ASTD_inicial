import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input, register_page
import plotly.graph_objects as go

from config import app_config

# Load Excel
archivo_excel = pd.ExcelFile('CO2.xlsx')

# Load sheets
data_hoja1 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_totals_by_country')

data_h1 = data_hoja1.melt(
    id_vars=['ISOcode', 'Country'],  # fixed columns
    var_name='Year',                 # new col
    value_name='CO2 Emissions'       # new col 
)

years = app_config['Year']

register_page(__name__, name='page3', path='/page3')

layout = html.Div([
    dcc.Dropdown(
            id='dropdown-year3',
            options=[{'label': year, 'value': year} for year in app_config['Year']],
            placeholder="Select a year"
        ),
    dcc.Graph(id='graph-world-map3'),  # Mantener solo el gráfico del mapa mundial
], style={'width': '48%', 'display': 'inline-block'})


@callback(
    Output('graph-world-map3', 'figure'),
    [Input('dropdown-year3', 'value')]
)
def update_world_map(selected_year):
    df_year = data_h1[data_h1['Year'] == selected_year]

    fig = go.Figure(data=go.Choropleth(
        locations=df_year['ISOcode'],
        locationmode='ISO-3',
        z=df_year['CO2 Emissions'],
        text=df_year['CO2 Emissions'],
        colorscale='Viridis',
        colorbar=dict(title="CO2 Emissions")
    ))

    fig.update_geos(projection_type="orthographic")
    fig.update_layout(
        title=f'CO2 Emissions by Country in {selected_year}',
        height=600,
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    return fig