# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import data as csvUtils

csvList = ['./data/prints.csv', './data/filament-usage.csv', './data/all-rolls.csv']

# Load csv files into dataframes
printHistory, filamentHistory, currentFilament = csvUtils.readData(csvList)

# Export csv files from dataframes
csvUtils.writeData(csvList, [printHistory, filamentHistory, currentFilament])

# Main program loop
runLoop = True
while runLoop:
    # Start action iteration
    print('Would you like to view current filament(1), update current filament(2), add a print(3), or quit(4)?')
    action = int(input())

    if action == 1:
        print(currentFilament)
    elif action == 2:
        print('2')
    elif action == 3:
        print('3')
    elif action == 4:
        print('Program ending')
        runLoop = False