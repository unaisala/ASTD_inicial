import pandas as pd

archivo_excel = pd.ExcelFile('CO2.xlsx')

# # Load sheets
data_hoja1 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_totals_by_country')
# data_hoja2 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_per_capita_by_countr')
data_hoja3 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_by_sector_and_countr')

data_1 = data_hoja1.melt(
    id_vars=['ISOcode', 'Country'],  # fixed columns
    var_name='Year',                 # new col
    value_name='CO2 Emissions'       # ew col 
)


# Cargar el archivo Excel
# data_1 = pd.read_excel('CO2.xlsx', sheet_name='fossil_CO2_totals_by_country')

# Obtener todos los países únicos en la columna 'Country'
countries = data_1['Country'].unique().tolist()  # Convertir a lista
years = data_1['Year'].unique().tolist()  # Convertir a lista


# Crear el archivo config.py
app_config = {
    'Country': countries,  # Lista de países únicos
    'Year': years  # Lista de años
    #'Year': list(range(1970, 2020 + 1))  # Años entre 1970 y 2020
}

data_3 = data_hoja3.melt(
    id_vars=['Sector', 'ISOcode', 'Country'],  # columnas fijas
    var_name='Year',                 # nueva columna
    value_name='CO2 Emissions'       # nueva columna 
)

grouped_data_sectors = data_3.groupby(['Sector', 'Year'])['CO2 Emissions'].mean().reset_index()