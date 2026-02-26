import data as csvUtils
import pandas as pd

def printFilamentData(path):
    # Get filament data
    filamentData = csvUtils.readData([path])

    # Print filament data or message
    if len(filamentData) > 1:
        print(filamentData)
    else:
        print('There is no active filament')

def updateFilament(path):
    # Get update type
    print("Would you like to add a new filament roll(1), update the status of current filament(2), or update time last dried for filament(3)?")
    updateType = int(input())

    # Start correct update type
    if updateType == 1:
        addRolls(path)
    elif updateType == 2:
        print()
    elif updateType == 3:
        print()

def actionThree():
    print('incomplete action 3')

def endProgram():
    # Print message
    print('Ending program')

    # End main loop
    return False

def addRolls(path):
    # Get data about roll
    print('What colour is the new roll')
    newColour = input()
    print('What material is the new roll')
    newMaterial = input()
    print('What company is the new roll from')
    newCompany = input()
    print('What size is the roll')
    newSize = int(input())
    print('What did the new roll cost')
    newPrice = float(input())
    print('When was this purchased (MM-DD-YYYY, or TODAY)')
    newDate = input()

    # Read CSV file
    filamentData = csvUtils.readData(['./data/allRolls.csv'])[0]

    # Compile information into a list
    newFilament = [len(filamentData), newColour, newMaterial, newCompany, newSize, newSize, None, newPrice, newDate, 'Waiting', None]
    newFilament = ['one', 'two', 'three', 'four', 5, 6.0, '7', '8', '9', '10', 'eleven']

    # Update dataframe and CSV file
    filamentData = csvUtils.addRow(newFilament, filamentData)
    csvUtils.writeData(['./data/allRolls.csv'], [filamentData])