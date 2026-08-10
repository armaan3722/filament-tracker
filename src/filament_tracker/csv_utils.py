from pathlib import Path
from typing import Any

import pandas as pd


def read_data(csv_paths: list[str | Path]) -> tuple[pd.DataFrame, ...]:
    # Empty dataframes object
    dataframes = []

    # Read multiple CSV files
    for path in csv_paths:
        dataframes.append(pd.read_csv(path))

    # Output as a tuple of dataframes
    return tuple(dataframes)


def write_data(csv_paths: list[str | Path], dataframes: list[pd.DataFrame]) -> None:
    for path, df in zip(csv_paths, dataframes):
        df.to_csv(path, index=False)


def add_row(data_to_add: list[Any], dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe.loc[len(dataframe)] = data_to_add
    return dataframe


def get_row(dataframe: pd.DataFrame, id_column: str, column_value: Any) -> pd.DataFrame:
    return dataframe.loc[dataframe[id_column] == column_value]


def change_row(dataframe: pd.DataFrame, row: int, value: list[Any]) -> pd.DataFrame:
    dataframe.loc[row] = value
    return dataframe


def get_cell(
    dataframe: pd.DataFrame,
    column_to_search: str,
    value_to_search_for: Any,
    column_to_get_value: str,
) -> Any:
    return dataframe.loc[
        dataframe[column_to_search] == value_to_search_for, column_to_get_value
    ].iloc[0]


def change_cell(
    dataframe: pd.DataFrame,
    column_to_search: str,
    value_to_search_for: Any,
    column_to_change: str,
    value_to_change_to: Any,
) -> pd.DataFrame:
    dataframe.loc[
        dataframe[column_to_search] == value_to_search_for, column_to_change
    ] = value_to_change_to
    return dataframe
