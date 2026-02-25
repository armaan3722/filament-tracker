import data as csvUtils

def printFilamentData(path):
    # Get filament data
    filamentData = csvUtils.readData([path])

    # Print filament data
    if len(filamentData) != 1:
        print(filamentData)
        print(len(filamentData))
    else:
        print('There is no active filament')

def actionTwo():
    print('incomplete action 2')

def actionThree():
    print('incomplete action 3')

def endProgram():
    # Print message
    print('Ending program')

    # End main loop
    return False