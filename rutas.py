import pandas as pd


def get_routes(dataframe):
    """
    Función que calcula las ventas totales por ruta
    :param dataframe: un dataframe que contiene la información original
    :return: el dataframe modificado
    """
    # Obtener la suma anual de las rutas
    dataframe = dataframe.drop(columns='direction')
    dataframe = dataframe.groupby(['origin', 'destination', 'year'], sort=False).agg(
        total_value=pd.NamedAgg(column='total_value', aggfunc='sum'),
        total_sales=pd.NamedAgg(column='total_value', aggfunc='count'))

    # Obtener el promedio del total_value por rutas
    dataframe = dataframe.reset_index().drop(columns='year')
    dataframe = dataframe.groupby(['origin', 'destination'], sort=False).agg(
        avg_total_value= pd.NamedAgg(column='total_value', aggfunc='mean') ,
        total_sales=pd.NamedAgg(column='total_sales', aggfunc='sum'))
    dataframe = dataframe.reset_index()

    return dataframe


def sort_routes_by_index(dataframe):
    """
    Funcipón que crea una columna que contiene el valor de un índice
    que ayudará a ordenar las rutas.
    :param dataframe: un dataframe que contiene a las rutas
    :return: el dataframe con los datos ordenados por el índice
    """

    # Obtener el valor máximo y mínimo de cada columna
    max_avg_total_value = dataframe['avg_total_value'].max()
    max_total_sales = dataframe['total_sales'].max()
    min_avg_total_value = dataframe['avg_total_value'].min()
    min_total_sales = dataframe['total_sales'].min()

    # Usar los datos y crear un índice para ordenar las rutas
    scaled_avg_total_value = (dataframe['avg_total_value'] - min_avg_total_value) / \
                             (max_avg_total_value - min_avg_total_value)
    scaled_total_sales = (dataframe['total_sales'] - min_total_sales) / (max_total_sales - min_total_sales)

    # obtengamos el promedio para hallar el índice
    dataframe['index'] =round( (scaled_avg_total_value + scaled_total_sales) / 2 , 3)

    dataframe = dataframe.sort_values(by='index', ascending=False)

    return dataframe
