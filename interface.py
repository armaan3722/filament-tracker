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

def addPrint(printPath, filamentPath, allPath):
    # Get print information
    print('What is the name of the print')
    printName = input()
    print('What date was it printed (MM-DD-YYYY)')
    printDate = input()
    print('How many different filaments were used')
    numberOfColours = int(input())

    # Get list of filament
    prints, filament, allRolls = csvUtils.readData([printPath, filamentPath, allPath])
    simplifiedRollInformation = csvUtils.getRow(allRolls, 'state', 'Active')[['filamentID', 'colour', 'material', 'company', 'remainingAmount', 'datePurchased']]

    # Update general information
    printID = len(prints)
    prints = csvUtils.changeRow(prints, printID, [printDate, printID, printName])

    # Save changes
    csvUtils.writeData([printPath], [prints])

    # Get filament usage information
    i = 0
    while i < numberOfColours:
        # Get filament used
        print(simplifiedRollInformation)
        print('What is one filament used ID')
        filamentUsedID = int(input())

        # Get time and amount used
        print('How much of this filament was used')
        filamentUsedAmount = float(input())
        print('How long did this filament take to print')
        filamentTimePrinting = input()

        # Update information
        filament = csvUtils.changeRow(filament, len(filament) + i, [filamentUsedID, printID, filamentUsedAmount, filamentTimePrinting])
        allRolls = csvUtils.changeCell(allRolls, 'filamentID', filamentUsedID, 'remainingAmount', int(csvUtils.getRow(allRolls, 'filamentID', filamentUsedID)['remainingAmount'][0]) - filamentUsedAmount)
        
        # Next iteration
        i += 1
    
    # Write to CSV
    csvUtils.writeData([filamentPath, allPath], [filament, allRolls])

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

def addProject(categoryPath, projectPath, statePath):
    # Read csv data
    allCategories, allProjects, allStates = csvUtils.readData([categoryPath, projectPath, statePath])

    # Create lists
    allDataframes = [allCategories, allProjects, allStates]
    allPaths = [categoryPath, projectPath, statePath]
    updateTypes = ['category', 'project', 'state']

    # Update category
    lastUpdate = None
    i = 0
    while i < 2:
        # Get information
        currentPath = allPaths[i]
        currentDataframe = allDataframes[i]
        currentUpdateType = updateTypes[i]

        # Write information
        print(currentDataframe)
        print(f'Enter a {currentUpdateType} ID or type A to add a new {currentUpdateType}')
        editType = input()

        # Do update
        if editType == 'A':
            print(f'What is the name of the new {currentUpdateType}')
            newUpdate = input()
            currentDataframe = updateRow(currentDataframe, newUpdate, currentUpdateType, lastUpdate)
            #currentDataframe = csvUtils.addRow([len(currentDataframe),newUpdate], currentDataframe)
            csvUtils.writeData([currentPath], [currentDataframe])
            break

        # Update edit type
        editType = int(editType)
        lastUpdate = editType
        allDataframes[i + 1] = csvUtils.getRow(allDataframes[i+1], f'{currentUpdateType}ID', editType)

        # Update counter
        i += 1

def updateRow(dataframe, newUpdate, updateType, lastUpdate):
    match updateType:
        case 'category':
            dataframe = csvUtils.addRow([len(dataframe),newUpdate], dataframe)
        case 'project' | 'state':
            dataframe = csvUtils.addRow([len(dataframe),lastUpdate,newUpdate], dataframe)
    
    return dataframe