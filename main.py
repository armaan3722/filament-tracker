# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import data as csvUtils

csvList = ['./data/prints.csv', './data/filament-usage.csv', './data/all-rolls.csv']

# Load csv files into dataframes
df1, df2, df3 = csvUtils.readData(csvList)

# Export csv files from dataframes
csvUtils.writeData(csvList, [df1, df2, df3])