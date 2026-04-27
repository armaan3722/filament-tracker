import csvUtils as csvUtils

# FILAMENT
def readFilament(filamentPath, dryerPath, dryerEventsPath):
    # Get filament information
    filament, dryers, dryerEvents = csvUtils.readData([filamentPath, dryerPath, dryerEventsPath])

    # Print data
    print('Filament')
    print(filament.to_string(index=False))

    # Get action
    print('\n\nWould you like to edit filament(1), add a drying event(2), or return to home(3)')
    action = int(input())

    match action:
        case 1:
            editFilament(filament, filamentPath)
        case 2:
            addDryingEvent(filament, filamentPath, dryers, dryerEvents, dryerEventsPath)
        case 3:
            print('Returning to home page')

def editFilament(filament, filamentPath):
    # Get filament to edit
    print(filament.to_string(index=False))
    print('Enter ID of filament to edit')
    filamentID = int(input())

    # Get value to edit
    print('Do you want to edit company(1), colour(2), material(3), diameter(4), starting amount(5), or state(6)')
    editType = int(input())
    print('Enter new value')
    newValue = input()

    match editType:
        case 1:
            column = 'filamentCompany'
        case 2:
            column = 'filamentColour'
        case 3:
            column = 'filamentMaterial'
        case 4:
            column = 'diameter'
        case 5:
            column = 'startingAmount'
        case 6:
            column = 'state'
    
    # Edit
    filament = csvUtils.changeCell(filament, 'filamentID', filamentID, column, newValue)
    csvUtils.writeData([filamentPath], [filament])

def addDryingEvent(filament, filamentPath, dryers, dryerEvents, dryerEventsPath):
    # Get filament roll dried
    print(filament.to_string(index=False))
    print('Enter ID of filament roll dried')
    filamentID = int(input())

    # Get dryer used
    print(dryers.to_string(index=False))
    print('Enter ID of filament dryer used')
    dryerID = int(input())
    
    # Get drying information
    print('How long was the filament dried')
    length = input()
    print('What temperature was the filament dried at')
    temp = input()
    print('When was the filament dried')
    date = input()

    # Reformat
    filament["dateLastDried"] = filament["dateLastDried"].astype(str)
    
    # Save to csv files
    filament = csvUtils.changeCell(filament, 'filamentID', filamentID, 'dateLastDried', date)
    dryerEvents = csvUtils.addRow([len(dryerEvents),filamentID,dryerID,temp,length,date], dryerEvents)
    csvUtils.writeData([filamentPath, dryerEventsPath], [filament, dryerEvents])

# REUSABLE SPOOLS
def readSpools(spoolPath):
    # Convert to csv
    spools = csvUtils.readData([spoolPath])[0]
    
    # Print spool information
    print('Reusable spools')
    print(spools.to_string(index=False))

    # Get action
    print('\n\nWould you like to edit a spool(1) or return to home page(2)')
    action = int(input())

    match action:
        case 1:
            editSpool(spools, spoolPath)
        case 2:
            print("Returning to home page")

def editSpool(spools, spoolPath):
    # Get spool to edit
    print("Enter ID of spool to edit")
    spoolID = int(input())

    # Get column to edit
    print("What would you like to set the type to")
    newValue = input()

    # Modify
    spools = csvUtils.changeCell(spools, 'spoolID', spoolID, 'type', newValue)
    csvUtils.writeData([spoolPath], [spools])

# PARTS
def readParts(partsPath):
    # Get information from csv
    parts = csvUtils.readData([partsPath])[0]

    # Print information
    print("Other parts information")
    print(parts.to_string(index=False))

    # Get next action
    print('Would you like to edit a part(1), or return to home page(2)')
    action = int(input())

    match action:
        case 1:
            editParts(parts, partsPath)
        case 2:
            print('Returning to home page')

def editParts(parts, partsPath):
    # Get ID of part to edit
    print(parts.to_string(index=False))
    print('Enter ID of part to edit')
    partID = int(input())

    # Get what to edit
    print('Would you like to edit the type(1), spec(2), or starting quantity(3)')
    editType = int(input())
    print('What is the new value')
    newValue = input()

    match editType:
        case 1:
            column = 'partType'
        case 2:
            column = 'partSpec'
        case 3:
            column = 'startingAmount'
    
    # Save change
    parts = csvUtils.changeCell(parts, 'partID', partID, column, newValue)
    csvUtils.writeData([partsPath], [parts])