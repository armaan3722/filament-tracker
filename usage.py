import csvUtils as csvUtils

# FILAMENT USAGE
def addFilamentUsage(projectsPath, categoriesPath, collectionsPath, printJobsPath, printerPath, amsPath, hotendPath, buildplatePath, filamentPath, filamentUsedPath):
    # Get dataframes
    projects, categories, collections, printJobs, printer, ams, hotend, buildplate, filament, filamentUsed = csvUtils.readData([projectsPath, categoriesPath, collectionsPath, printJobsPath, printerPath, amsPath, hotendPath, buildplatePath, filamentPath, filamentUsedPath])
    
    # Get project information
    print(projects)
    print('Enter project ID of print')
    projectID = input()

    if projectID != '':
        projectID = int(projectID)
    else:
        projectID = None

    # Get collection information, either pick a collection or create a new one
    print('Do you want to select a collection(1), or create a new collection(2)')
    collectionAction = int(input())

    if collectionAction == 1:
        print(printJobs.to_string(index=False))
        print('\n\n')
        print(collections.to_string(index=False))
        print('\n\nEnter collection ID')
        collectionID = int(input())
    else:
        print('\n\nWhat is the new collection name')
        collectionName = input()
        print('Enter purpose')
        purpose = input()
        print('Enter stage')
        stage = input()
        print(categories.to_string(index=False))
        print('Enter category ID')
        categoryID = input()
        print('Enter version')
        version = input()
        print('Enter revision')
        revision = input()
        print('Does this collection have configs (T/f)')
        hasConfig = input()
        print('What quantity does this collection produce')
        quantityProduced = input()

        # Changing value types
        if hasConfig == 'T':
            hasConfig = True
        else:
            hasConfig = False

        # Handle null values
        testArray = [collectionName,purpose,stage,categoryID,version,revision,hasConfig,quantityProduced]

        i = 0
        while i < len(testArray):
            if testArray[i] == '':
                testArray[i] = None
            i += 1
        
        # Save data
        collectionID = len(collections)
        collections = csvUtils.addRow([len(collections),collectionName,projectID,testArray[1],testArray[2],testArray[3],testArray[4],testArray[5],testArray[6],testArray[7]], collections)
        csvUtils.writeData([collectionsPath], [collections])

    # Get the rest of the print job and filament usage information

    # Print job information
    print('Enter the date printed')
    date = input()
    print('Enter the length of print')
    time = input()
    print('Enter the time taken to prepare print')
    prepTime = input()
    print(printer.to_string(index=False))
    print('Enter printer ID')
    printerID = int(input())
    print(ams.to_string(index=False))
    print('Enter ams ID if applicable')
    amsID = int(input())
    print(hotend.to_string(index=False))
    print('Enter hotend ID')
    hotendID = int(input())
    print(buildplate.to_string(index=False))
    print('Enter buildplate ID')
    buildplateID = int(input())

    # Get filament used
    print('How many different spools of filament were used')
    spoolsUsed = int(input())

    i = 0
    while i < spoolsUsed:
        # Get information
        print(filament.to_string(index=False))
        print('Enter ID of filament used')
        filamentID = int(input())
        print('Enter amount of filament used in grams')
        filamentAmountPrinted = float(input())

        # Update information
        filamentUsed = csvUtils.addRow([filamentID,filamentAmountPrinted,len(printJobs)], filamentUsed)

        previousFilamentLeft = csvUtils.getCell(filament, 'filamentID', filamentID, 'amountLeft')
        previousFilamentLeft -= filamentAmountPrinted
        
        filament = csvUtils.changeCell(filament, 'filamentID', filamentID, 'amountLeft', previousFilamentLeft)

        i += 1

    # Update filament left and printer hours used
    printJobs = csvUtils.addRow([len(printJobs),date,time,prepTime,printerID,amsID,hotendID,buildplateID,collectionID,None,None,None,None,None,None], printJobs)

    printerSeconds = csvUtils.getCell(printer, 'printerID', printerID, 'printerSecondsUsed')
    printerOperationSeconds = csvUtils.getCell(printer, 'printerID', printerID, 'printerSecondsInOperation')

    arrayTime = time.split()
    arrayPrepTime = prepTime.split()

    printJobSeconds = (
        int(arrayTime[0]) * 86400 + 
        int(arrayTime[1]) * 3600 + 
        int(arrayTime[2]) * 60 +
        int(arrayTime[3])
    )

    printJobPrepSeconds = (
        int(arrayPrepTime[0]) * 86400 +
        int(arrayPrepTime[1]) * 3600 + 
        int(arrayPrepTime[2]) * 60 +
        int(arrayPrepTime[3]) 
    )

    printerSeconds += (printJobSeconds - printJobPrepSeconds)
    printerOperationSeconds += printJobSeconds

    printer = csvUtils.changeCell(printer, 'printerID', printerID, 'printerSecondsUsed', printerSeconds)
    printer = csvUtils.changeCell(printer, 'printerID', printerID, 'printerSecondsInOperation', printerOperationSeconds)

    csvUtils.writeData([printJobsPath, filamentUsedPath, printerPath, filamentPath], [printJobs, filamentUsed, printer, filament])

    # Add code for creation and selection of configs later

# NON PRINTED PARTS
def addParts(projectsPath, categoriesPath, collectionsPath):
    # Get dataframes
    projects, categories, collections = csvUtils.readData([projectsPath, categoriesPath, collectionsPath])

    # Get project information
    print(projects.to_string(index=False))
    print('Enter project ID')
    projectID = input()

    if projectID != '':
        projectID = int(projectID)
    else:
        projectID = None
    
    # Get collection
    print('\n\nWould you like to select a collection(1) or create a new collection(2)')
    collectionAction = int(input())

    match collectionAction:
        case 1:
            print('\n\n' + collections.to_string(index=False))
            print('Enter collection ID')
            collectionID = int(input())
        case 2:
            print('\n\n')
            print('Enter collection name')
            collectionName = input()
            if collectionName == '': collectionName = None
            print('\n')

            print(categories.to_csv(index=False))
            print('Enter category ID')
            categoryID = int(input())
            if categoryID == '': categoryID = None
            print('\n')

            print('Enter purpose of collection')
            purpose = input()
            if purpose == '': purpose = None
            print('Enter stage of collection')
            stage = input()
            if stage == '': stage = None
            print('\n')

            print('Enter version')
            version = int(input())
            if version == '': version = None
            print('Enter revision')
            revision = int(input())
            if revision == '': revision = None
            print('\n')

            print('Does this have a config (T/f)')
            hasConfig = input()
            if hasConfig == 'T':
                hasConfig = True
                print('What quantity does it produce')
                quantityProduced = input()
            else: 
                hasConfig = False
                quantityProduced = None
            
            collectionID = len(collections)
            collections = csvUtils.addRow([collectionID,collectionName,projectID,purpose,stage,categoryID,version,revision,hasConfig,quantityProduced], collections)
            csvUtils.writeData([collectionsPath], [collections])