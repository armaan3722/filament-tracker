import data as csvUtils
import pandas as pd

def printFilamentData(path):
    # Get filament data
    filamentData = csvUtils.readData([path])[0]

    # Print filament data or message
    if len(filamentData) > 0:
        print(filamentData.to_string(index=False))
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
        updateRolls(path)
    elif updateType == 3:
        updateTimeDried(path)

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

    # Update dataframe and CSV file
    filamentData = csvUtils.addRow(newFilament, filamentData)
    csvUtils.writeData([path], [filamentData])

def updateRolls(path):
    # Get filament information
    allRolls = csvUtils.readData([path])[0]
    simplifiedRollInformation = allRolls[['filamentID', 'colour', 'material', 'company', 'remainingAmount', 'state']]
    
    # Get roll to update
    print('Which filament roll would you like to update, enter ID')
    print(simplifiedRollInformation.to_string(index=False))
    selectedRoll = int(input())

    # Get value to modify to
    print(f'Current state: {csvUtils.getRow(allRolls, 'filamentID', selectedRoll)['state']}')
    print('What would you like to set the state to waiting(1), active(2), or finished(3)')
    updatedState = int(input())

    # Update row
    if updatedState == 1:
        updatedState = 'Waiting'
    elif updatedState == 2:
        updatedState = 'Active'
    elif updatedState == 3:
        updatedState = 'Finished'

    allRolls = csvUtils.changeCell(allRolls, 'filamentID', selectedRoll, 'state', updatedState)

    # Save data
    csvUtils.writeData([path], [allRolls])

def updateTimeDried(path):
    # Get last time dried
    allRolls = csvUtils.readData([path])[0]
    allRolls['lastTimeDried'] = allRolls['lastTimeDried'].astype('string')
    simplifiedRollInformation = csvUtils.getRow(allRolls[['filamentID', 'colour', 'material', 'company', 'remainingAmount', 'lastTimeDried', 'state']], 'state', 'Active')

    # Get roll to update
    print('Which roll would you like to update, enter ID number')
    print(simplifiedRollInformation)
    selectedRoll = int(input())

    # Get time dried
    print(f'When was that roll dried (MM-DD-YYYY)')
    timeDried = input()

    # Update table
    allRolls = csvUtils.changeCell(allRolls, 'filamentID', selectedRoll, 'lastTimeDried', timeDried)

    # Save table
    csvUtils.writeData([path], [allRolls])