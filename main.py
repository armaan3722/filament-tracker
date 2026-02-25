# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import data as csvUtils
import interface as io

# CSV file paths
PRINT_HISTORY_PATH = './data/prints.csv'
FILAMENT_HISTORY_PATH = './data/filament-usage.csv'
CURRENT_FILAMENT_PATH = './data/all-rolls.csv'
ALL_CSV_FILES = [PRINT_HISTORY_PATH, FILAMENT_HISTORY_PATH, CURRENT_FILAMENT_PATH]

# Load csv files into dataframes
printHistory, filamentHistory, currentFilament = csvUtils.readData(ALL_CSV_FILES)

# Export csv files from dataframes
csvUtils.writeData(ALL_CSV_FILES, [printHistory, filamentHistory, currentFilament])

# Main program loop
runLoop = True
while runLoop:
    # Start action iteration
    print('Would you like to view current filament(1), update current filament(2), add a print(3), or quit(4)?')
    action = int(input())

    # Run correct function
    if action == 1:
        # Print filament data
        io.printFilamentData(CURRENT_FILAMENT_PATH)
    elif action == 2:
        io.actionTwo()
    elif action == 3:
        io.actionThree()
    elif action == 4:
        # End program
        runLoop = io.endProgram()