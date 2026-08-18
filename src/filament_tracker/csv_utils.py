from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pandas as pd


def read_data(
    csv_paths: Sequence[str | Path | dict[str, Any]],
) -> tuple[pd.DataFrame, ...]:
    """Read the data from multiple csv files.

    Reads the csv files at the given paths, and outputs a tuple with
    dataframes containing the data from those files.
    Accepts paths directly or dicts with a 'filepath' key.

    Args:
        csv_paths: The paths to get csv files from, or dicts containing
            'filepath' keys.

    Returns:
        A tuple of dataframes with the data from the csv files.
    """
    # Empty dataframes object
    dataframes = []

    # Read multiple CSV files
    for item in csv_paths:
        path = item["filepath"] if isinstance(item, dict) else item
        dataframes.append(pd.read_csv(path))

    # Output as a tuple of dataframes
    return tuple(dataframes)


def write_data(
    csv_paths: Sequence[str | Path | dict[str, Any]], dataframes: list[pd.DataFrame]
) -> None:
    """Write multiple dataframes to multiple csv files.

    Iterates through the csv_paths and dataframes lists, writing each
    dataframe to the path with the same index.
    Accepts paths directly or dicts with a 'filepath' key.

    Args:
        csv_paths: The list of paths to write dataframes to, or dicts
            containing 'filepath' keys.
        dataframes: The dataframes.

    Notes: The csv_paths and dataframes lists must be identical length.
    """
    for item, df in zip(csv_paths, dataframes):
        path = item["filepath"] if isinstance(item, dict) else item
        df.to_csv(path, index=False)


def add_row(data_to_add: list[Any], dataframe: pd.DataFrame) -> pd.DataFrame:
    """Adds a row to a dataframe.

    Args:
        data_to_add: The data for the row to be added.
        dataframe: The dataframe to add a row to.

    Returns:
        The dataframe with the row added.
    """
    dataframe.loc[len(dataframe)] = data_to_add
    return dataframe


def get_row(dataframe: pd.DataFrame, id_column: str, column_value: Any) -> pd.DataFrame:
    """Get a row from a dataframe.

    Gets a row from a dataframe based on an id_column and value to
    search for.

    Args:
        dataframe: The dataframe to search for a row from.
        id_column: The column to search to find the desired row.
        column_value: The value in the id_column to search for.

    Returns:
        The first row that has a value in id_column that matches
            column_value.
    """
    return dataframe.loc[dataframe[id_column] == column_value]


def change_row(dataframe: pd.DataFrame, row: int, value: list[Any]) -> pd.DataFrame:
    """Modifies a row from a dataframe

    Overwrites a row in a dataframe with a new set of data.

    Args:
        dataframe: The dataframe to modify.
        row: The row number to overwrite.
        value: The data to be written into the row.

    Returns:
        The dataframe with the modified row.
    """
    dataframe.loc[row] = value
    return dataframe


def get_cell(
    dataframe: pd.DataFrame,
    column_to_search: str,
    value_to_search_for: Any,
    column_to_get_value: str,
) -> Any:
    """Get the value of a cell in a dataframe.

    Finds the desired row by looking for the first row in the dataframe
    that has a value in column_to_search that matches
    value_to_search_for.  Then, gets the value of column_to_get_value
    for that row.

    Args:
        dataframe: The dataframe to search
        column_to_search: The column used to identify the desired row.
        value_to_search_for: The value to search for in that column.
        column_to_get_value: The column to get the value from.

    Returns:
        The value of the column given in the row found with the search parameters.
    """
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
    """Change the value of a cell in a dataframe.

    First, finds the desired row by looking at the column_to_search and
    value_to_search_for.  Second, find the value in that row to access
    based on column_to_change.  Finally, change that value to
    value_to_change_to.

    Args:
        dataframe: The dataframe to change a cell in.
        column_to_search: The column to use to identify the row.
        value_to_search_for: The value to find in the id column.
        column_to_change: The column to change a value in.
        value_to_change_to: The value to change the cell to.

    Returns:
        The dataframe with the modified cell.
    """
    dataframe.loc[
        dataframe[column_to_search] == value_to_search_for, column_to_change
    ] = value_to_change_to
    return dataframe
