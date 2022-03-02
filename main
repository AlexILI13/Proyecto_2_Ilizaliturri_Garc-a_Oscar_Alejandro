import pandas as pd
import rutas as ru
import sys


# Consideremos lo datos de synergy_logistics, sin considerar por el momento el register_id

synergy_logistics_info_df = pd.read_csv('synergy_logistics_database.csv', usecols=lambda x: x != 'register_id')


def option_1():
    """
    Función que obtiene los 10 países que más importan y exportan y los muestran.
    """
    # copiemos el dataframe
    option_1_df = synergy_logistics_info_df.copy()
    option_1_df.drop(columns=['product', 'transport_mode', 'date', 'company_name'], inplace=True)

    # consideremos dos dataframes, uno para importaciones y otro para exportaciones
    option_1_df_exports = option_1_df[option_1_df['direction'] == 'Exports']
    option_1_df_imports = option_1_df[option_1_df['direction'] == 'Imports']

    option_1_df_exports = ru.get_routes(option_1_df_exports)
    option_1_df_imports = ru.get_routes(option_1_df_imports)

    option_1_df_exports = ru.sort_routes_by_index(option_1_df_exports).reset_index(drop=True)
    option_1_df_imports = ru.sort_routes_by_index(option_1_df_imports).reset_index(drop=True)

    option_1_df_exports.index = option_1_df_exports.index + 1
    option_1_df_imports.index = option_1_df_imports.index + 1
    print('10 rutas que más exportan:')
    print(option_1_df_exports[:10])
    print('\n')
    print('10 rutas que más importan:')
    print(option_1_df_imports[:10])


def option_2():
    """
    Función que ordena los dataframe por medios de transporte, su valor total y lo muestra
    """
    option_2_df = synergy_logistics_info_df.copy()
    option_2_df = option_2_df.drop(columns=['origin', 'destination', 'year', 'date', 'product', 'company_name'])
    print(option_2_df.groupby(['transport_mode', 'direction']).sum().sort_values(by='total_value', ascending=False))
    print("\n")
    print(option_2_df.groupby(['transport_mode']).sum().sort_values(by='total_value', ascending=False))


def option_3():
    """
    Funcion que calcula el valor total acumulado de cada país y lo muestra
    
    """
    option_3_df = synergy_logistics_info_df.copy()

    # obtendremos el origen y el destino y crearemos una nueva columna
    option_3_df['country'] = option_3_df.apply(
        lambda row: row['origin'] if row['direction'] == 'Exports' else row['destination'], axis=1)
    option_3_df = option_3_df[['country', 'total_value']]
    option_3_df = option_3_df.groupby('country').sum()
    option_3_df = option_3_df.sort_values(by='total_value', ascending=False)
    option_3_df['cumulative_percentage'] = 100 * option_3_df['total_value'].cumsum() / option_3_df['total_value'].sum()
    print(round(option_3_df , 3))


def analysis(option):
    """
    Esta función nos permitirá elegir los datos que buscamos
    """
    opciones = {
        1: option_1,
        2: option_2,
        3: option_3,
    }
    func = opciones.get(option, "Por favor elija un número del 1 al 3 únicamente")
    return func()


final = 'n'

while final != ('s' or 'S'):
    print('''
    Opciones diponibles:
        1.- Obtener las 10 rutas de importación y exportación más demandadas.
        2.- los medios de tranporte usados por la empresa ordenados según sus ingresos 
        3.- Total de ingresos de las importaciones y exportaciones y los países que generan el 80% de ingresos de la compañia.
    ''')

    analysis(int(input('Escriba la opción que requiera: ')))
    final = input('¿Desea abandonar? (s/n): ')
