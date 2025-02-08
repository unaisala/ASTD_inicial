# import pandas as pd
# from dash import Dash, dcc, html, callback, Output, Input, register_page
# import plotly.express as px
# from config import app_config

# # Cargar datos globalmente
# archivo_excel = pd.ExcelFile('CO2.xlsx')
# data_hoja1 = pd.read_excel(archivo_excel, sheet_name='fossil_CO2_totals_by_country')
# data_hoja2 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_per_capita_by_countr')
# data_hoja3 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_by_sector_and_countr')

# # Convertir los datos a formato largo
# data_h1 = data_hoja1.melt(
#     id_vars=['ISOcode', 'Country'],
#     var_name='Year',
#     value_name='CO2 Emissions'
# )

# # Establecer configuraciones de países y años desde la configuración
# countries = app_config['Country']
# years = app_config['Year']

# # Register page en lugar de app
# register_page(__name__, name='home', path='/')

# layout = html.Div([ 
#     html.Div([
#         dcc.Dropdown(
#             id='dropdown-country',
#             options=[{'label': pais, 'value': pais} for pais in app_config['Country']],
#             placeholder="Select a country"
#         ),
#         dcc.Graph(id='graph-country'),
#     ], style={'width': '48%', 'display': 'inline-block'}),
# ])

# # Callback para actualizar el gráfico por país
# @callback(
#     Output('graph-country', 'figure'),
#     [Input('dropdown-country', 'value')]
# )
# def update_graph_country(selected_country):
#     if not selected_country:
#         return {}  # Retorna un gráfico vacío si no se selecciona un país
    
#     # Filtrar los datos para el país seleccionado
#     df_country = data_h1[data_h1['Country'] == selected_country]

#     # Calcular la media global de emisiones de CO2 por año
#     df_global = data_h1.groupby('Year')['CO2 Emissions'].mean().reset_index()
#     df_global['Country'] = 'Global'

#     # Combinar los datos del país seleccionado con la media global
#     df_combined = pd.concat([df_country, df_global])

#     # Crear gráfico de línea con la media global incluida
#     fig_country = px.line(
#         df_combined, x='Year', y='CO2 Emissions',
#         color='Country',  # Diferenciar por país (país seleccionado vs global)
#         title=f'CO2 Emissions in {selected_country} and Global Average per Year',
#         labels={'CO2 Emissions': 'CO2 Emissions (tons)', 'Year': 'Year'},
#         markers=True
#     )

#     return fig_country




import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input, register_page
import plotly.express as px
from config import app_config

# Cargar datos globalmente
archivo_excel = pd.ExcelFile('CO2.xlsx')
data_hoja1 = pd.read_excel(archivo_excel, sheet_name='fossil_CO2_totals_by_country')
data_hoja2 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_per_capita_by_countr')
data_hoja3 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_by_sector_and_countr')

# Convertir los datos a formato largo
data_h1 = data_hoja1.melt(
    id_vars=['ISOcode', 'Country'],
    var_name='Year',
    value_name='CO2 Emissions'
)

data_h2 = data_hoja2.melt(
    id_vars=['ISOcode', 'Country'],
    var_name='Year',
    value_name='CO2 Emissions'
)

data_h3 = data_hoja3.melt(
    id_vars=['ISOcode', 'Country'],
    var_name='Year',
    value_name='CO2 Emissions'
)

# Establecer configuraciones de países y años desde la configuración
countries = app_config['Country']
years = app_config['Year']

# Register page en lugar de app
register_page(__name__, name='home', path='/')

layout = html.Div([ 
    html.Div([
        dcc.Dropdown(
            id='dropdown-country',
            options=[{'label': pais, 'value': pais} for pais in app_config['Country']],
            placeholder="Select a country"
        ),
        dcc.Graph(id='graph-country1'),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='graph-country2'),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='graph-country3'),
    ], style={'width': '100%', 'display': 'inline-block'}),
])

# Callback para actualizar el gráfico por país - Hoja 1
@callback(
    Output('graph-country1', 'figure'),
    [Input('dropdown-country', 'value')]
)
def update_graph_country1(selected_country):
    if not selected_country:
        return {}  # Retorna un gráfico vacío si no se selecciona un país
    
    # Filtrar los datos para el país seleccionado
    df_country = data_h1[data_h1['Country'] == selected_country]

    # Calcular la media global de emisiones de CO2 por año
    df_global = data_h1.groupby('Year')['CO2 Emissions'].mean().reset_index()
    df_global['Country'] = 'Global'

    # Combinar los datos del país seleccionado con la media global
    df_combined = pd.concat([df_country, df_global])

    # Crear gráfico de línea con la media global incluida
    fig_country = px.line(
        df_combined, x='Year', y='CO2 Emissions',
        color='Country',  # Diferenciar por país (país seleccionado vs global)
        title=f'CO2 Emissions in {selected_country} and Global Average per Year (Total CO2)',
        labels={'CO2 Emissions': 'CO2 Emissions (tons)', 'Year': 'Year'},
        markers=True
    )

    return fig_country

# Callback para actualizar el gráfico por país - Hoja 2 (sin global)
@callback(
    Output('graph-country2', 'figure'),
    [Input('dropdown-country', 'value')]
)
def update_graph_country2(selected_country):
    if not selected_country:
        return {}  # Retorna un gráfico vacío si no se selecciona un país
    
    # Filtrar los datos para el país seleccionado
    df_country = data_h2[data_h2['Country'] == selected_country]

    # Crear gráfico de línea solo con el país seleccionado
    fig_country = px.line(
        df_country, x='Year', y='CO2 Emissions',
        title=f'CO2 Emissions per Capita in {selected_country} per Year',
        labels={'CO2 Emissions': 'CO2 Emissions per Capita (tons)', 'Year': 'Year'},
        markers=True
    )

    return fig_country

# Callback para actualizar el gráfico por país - Hoja 3
@callback(
    Output('graph-country3', 'figure'),
    [Input('dropdown-country', 'value')]
)
def update_graph_country3(selected_country):
    if not selected_country:
        return {}  # Retorna un gráfico vacío si no se selecciona un país
    
    # Filtrar los datos para el país seleccionado
    df_country = data_h3[data_h3['Country'] == selected_country]

    # Calcular la media global de emisiones de CO2 por año
    df_global = data_h3.groupby('Year')['CO2 Emissions'].mean().reset_index()
    df_global['Country'] = 'Global'

    # Combinar los datos del país seleccionado con la media global
    df_combined = pd.concat([df_country, df_global])

    # Crear gráfico de línea con la media global incluida
    fig_country = px.line(
        df_combined, x='Year', y='CO2 Emissions',
        color='Country',  # Diferenciar por país (país seleccionado vs global)
        title=f'CO2 Emissions by Sector in {selected_country} and Global Average per Year',
        labels={'CO2 Emissions': 'CO2 Emissions by Sector (tons)', 'Year': 'Year'},
        markers=True
    )

    return fig_country

