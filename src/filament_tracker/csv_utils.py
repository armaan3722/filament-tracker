import pandas as pd


def read_data(csv_paths):
    # Empty dataframes object
    dataframes = []

    # Read multiple CSV files
    for path in csv_paths:
        dataframes.append(pd.read_csv(path))

    # Output as a tuple of dataframes
    return tuple(dataframes)


def write_data(csv_paths, dataframes):
    for path, df in zip(csv_paths, dataframes):
        df.to_csv(path, index=False)


def add_row(data_to_add, dataframe):
    dataframe.loc[len(dataframe)] = data_to_add
    return dataframe


def get_row(dataframe, id_column, column_value):
    return dataframe.loc[dataframe[id_column] == column_value]


def change_row(dataframe, row, value):
    dataframe.loc[row] = value
    return dataframe


def get_cell(dataframe, column_to_search, value_to_search_for, column_to_get_value):
    return dataframe.loc[
        dataframe[column_to_search] == value_to_search_for, column_to_get_value
    ].iloc[0]


def change_cell(
    dataframe,
    column_to_search,
    value_to_search_for,
    column_to_change,
    value_to_change_to,
):
    dataframe.loc[
        dataframe[column_to_search] == value_to_search_for, column_to_change
    ] = value_to_change_to
    return dataframe
