import geopandas as gpd
import pandas as pd 
import numpy as np
import plotly.express as px

from config import app_config

def update_graph_country(selected_country):

    data_hoja1 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_totals_by_country')
    data_h1 = data_hoja1.melt(
        id_vars=['ISOcode', 'Country'],  # fixed columns
        var_name='Year',                 # new col
        value_name='CO2 Emissions'       # ew col 
    )

    if selected_country is None:
        return {}  # Devuelve un gráfico vacío si no se selecciona ningún país

    # Filtrar datos para el país seleccionado
    df_country = data_h1[data_h1['Country'] == selected_country]

    # Crear gráfico de línea
    fig_country = px.line(
        df_country, x='Year', y='CO2 Emissions',
        title=f'CO2 emissions in {selected_country} per year',
        labels={'CO2 Emissions': 'CO2 Emissions (tons)'}
    )
    return fig_country


def update_graph_year(selected_year):

    data_hoja1 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_totals_by_country')
    data_h1 = data_hoja1.melt(
        id_vars=['ISOcode', 'Country'],  # fixed columns
        var_name='Year',                 # new col
        value_name='CO2 Emissions'       # ew col 
    )
    
    if selected_year is None:
        return {}  # Devuelve un gráfico vacío si no se selecciona ningún año

    # Filtrar datos para el año seleccionado
    df_year = data_h1[data_h1['Year'] == selected_year]

    # Crear gráfico de barras
    fig_year = px.bar(
        df_year, x='Country', y='CO2 Emissions',
        title=f'CO2 emissions in {selected_year} per country',
        labels={'CO2 Emissions': 'CO2 emissions(tons)'}
    )
    return fig_year