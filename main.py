# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import data as csvUtils
import interface as io

# CSV file paths
PRINT_HISTORY_PATH = './data/prints.csv'
FILAMENT_HISTORY_PATH = './data/filament-usage.csv'
CURRENT_FILAMENT_PATH = './data/all-rolls.csv'
CATEGORY_HISTORY_PATH = './data/categories.csv'
PROJECT_HISTORY_PATH = './data/projects.csv'
STATE_HISTORY_PATH = './data/states.csv'
COLLECTION_HISTORY_PATH = './data/collections.csv'
REVISION_HISTORY_PATH = './data/revisions.csv'
ITERATION_HISTORY_PATH = './data/iterations.csv'

# Main program loop
runLoop = True
while runLoop:
    # Start action iteration
    print('Would you like to view current filament(1), update current filament(2), add a print(3), view current projects(4), add a project(5), or quit(6)?')
    action = int(input())

    # Run correct function
    if action == 1:
        # Print filament data
        io.printFilamentData(CURRENT_FILAMENT_PATH)
    elif action == 2:
        io.updateFilament(CURRENT_FILAMENT_PATH)
    elif action == 3:
        io.addPrint(PRINT_HISTORY_PATH, FILAMENT_HISTORY_PATH, CURRENT_FILAMENT_PATH)
    elif action == 4:
        print()
    elif action == 5:
        print()
    elif action == 6:
        # End program
        runLoop = io.endProgram()