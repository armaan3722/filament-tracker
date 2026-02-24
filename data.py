import pandas as pd

def readData(csvPaths):
    dataframes = []

    for path in csvPaths:
        dataframes.append(pd.read_csv(path))
    
    return tuple(dataframes)

def writeData(csvPaths, dataframes):
    for path, df in zip(csvPaths, dataframes):
        df.to_csv(path, index=False)