import pandas as pd

def readData(csvPaths):
    # Empty dataframes object
    dataframes = []

    # Read multiple CSV files
    for path in csvPaths:
        dataframes.append(pd.read_csv(path))
    
    # Output as a tuple of dataframes
    return tuple(dataframes)

def writeData(csvPaths, dataframes):
    for path, df in zip(csvPaths, dataframes):
        df.to_csv(path, index=False)

def addRow(dataToAdd, dataframe):
    dataframe.loc[len(dataframe)] = dataToAdd
    return dataframe

def getRow(dataframe, IDColumn, columnValue):
    return dataframe.loc[dataframe[IDColumn] == columnValue]

def changeRow(dataframe, row, value):
    dataframe.loc[row] = value
    return dataframe

def getCell(dataframe, columnToSearch, valueToSearchFor, columnToGetValue):
    return dataframe.loc[dataframe[columnToSearch] == valueToSearchFor, columnToGetValue].iloc[0]

def changeCell(dataframe, columnToSearch, valueToSearchFor, columnToChange, valueToChangeTo):
    dataframe.loc[dataframe[columnToSearch] == valueToSearchFor, columnToChange] = valueToChangeTo
    return dataframe