# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import data as csvUtils

csvList = ['./data/prints.csv', './data/filament-usage.csv', './data/all-rolls.csv']

# Load csv files into dataframes
printHistory = pd.read_csv('./data/prints.csv')
filamentUsed = pd.read_csv('./data/filament-usage.csv')
filamentOverview = pd.read_csv('./data/all-rolls.csv')

df1, df2, df3 = csvUtils.readData(csvList)