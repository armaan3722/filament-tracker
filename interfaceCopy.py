# Import modules
import data as csvUtils
import pandas as pd

# Get printer information
def readPrinter(printerPath, printerMaintenancePath):
    # Get csv files
    printer, printerMaintenance = csvUtils.readData([printerPath, printerMaintenancePath])

    # Print dataframes
    print("Printers:")
    print(printer.to_string(index=False))
    print('\n\nPrinter maintenance history:')
    print(printerMaintenance.to_string(index=False))

    # Update
    print('\n\nWould you like to edit a printer(1), create maintenance event(2), or go back to home page(3)')
    action = int(input())

    match action:
        case 1:
            editPrinter(printer, printerPath)
        case 2:
            updatePrinterMaintenance(printer, printerMaintenance, printerMaintenancePath)
        case 3:
            print('Returning to home page')

def addPrinter(printer, path, purchases, purchasesPath, purchaseID):
    # Get new printer information
    print('What is the new printer company')
    newPrinterCompany = input()
    print('What is the new printer model')
    newPrinterModel = input()
    print('What is the new printer name')
    newPrinterName = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the new printer cost')
    newPrinterCost = input()
    print('What is the new printer date purchased')
    newPrinterDate = input()
    print('What is the new printer date arrived')
    newPrinterArrivalDate = input()

    # Update dataframes
    printer = csvUtils.addRow([len(printer),newPrinterName,newPrinterCompany,newPrinterModel,0], printer)
    purchases = csvUtils.addRow([purchaseID,'Printer',seller,len(printer)-1,newPrinterDate,newPrinterArrivalDate,newPrinterCost], purchases)

    # Save
    csvUtils.writeData([path, purchasesPath], [printer, purchases])

def editPrinter(printer, path):
    # Get printer to edit
    print(printer.to_string(index=False))
    print('\nEnter ID of printer to edit')
    printerID = int(input())

    # Get what to edit
    print(csvUtils.getRow(printer, 'printerID', printerID))
    print('Do you want to edit the name(1), company(2), or model(3)')
    editType = int(input())
    print('What is the new value')
    newValue = input()

    # Save edit
    match editType:
        case 1:
            column = 'printerName'
        case 2:
            column = 'printerCompany'
        case 3:
            column = 'printerModel'
    
    printer = csvUtils.changeCell(printer, 'printerID', printerID, column, newValue)
    csvUtils.writeData([path], [printer])

def updatePrinterMaintenance(printer, maintenance, maintenancePath):
    # Get printer for maintenance
    print(printer.to_string(index=False))
    print('\nEnter ID of printer for maintenance event')
    printerID = int(input())

    # Get maintenance type
    print('Which maintenance was done, automatic calibration(1) or firmware update(2)')
    eventType = int(input())

    firmwareVersion = None
    match eventType:
        case 1:
            eventType = 'Automatic Calibration'
        case 2:
            eventType = 'Firmware Update'
            print('What version was it updated to')
            firmwareVersion = input()

    # Get date
    print('What date did this maintenance event happen')
    eventDate = input()
        
    # Save to file
    maintenance = csvUtils.addRow([len(maintenance),printerID,eventDate,eventType,firmwareVersion],maintenance)
    csvUtils.writeData([maintenancePath], [maintenance])

def readHotend(hotendPath, hotendMaintenancePath):
    # Read csv files
    hotend, hotendMaintenance = csvUtils.readData([hotendPath, hotendMaintenancePath])

    # Print information
    print('Hotends:')
    print(hotend.to_string(index=False))
    print('\n\nHotend maintenance history:')
    print(hotendMaintenance.to_string(index=False))

    # Update
    print('\n\nWould you like to edit a hotend(1), create a maintenance event(2), or return to home(3)')
    action = int(input())

    match action:
        case 1:
            editHotend(hotend, hotendPath)
        case 2:
            updateHotendMaintenance(hotend, hotendMaintenance, hotendMaintenancePath)
        case 3:
            print('Returning to home page')

def addHotend(hotend, hotendPath, purchases, purchasesPath, purchaseID):
    # Get hotend to add
    print('What is the new hotend company')
    newHotendCompany = input()
    print('What is the new hotend size')
    newHotendSize = input()
    print('What is the new hotend material')
    newHotendMaterial = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    newHotendDate = input()
    print('What is the date arrived')
    newHotendArrivalDate = input()
    print('What is the new hotend cost')
    newHotendCost = input()

    # Update dataframes
    hotend = csvUtils.addRow([len(hotend),newHotendCompany,newHotendSize,newHotendMaterial,'Passive'], hotend)
    purchases = csvUtils.addRow([purchaseID,'Hotend',seller,len(hotend)-1,newHotendDate,newHotendArrivalDate,newHotendCost], purchases)
    csvUtils.writeData([hotendPath, purchasesPath], [hotend, purchases])

def editHotend(hotend, hotendPath):
    # Get hotend to edit
    print(hotend.to_string(index=False))
    print('\nEnter ID of hotend to edit')
    hotendID = int(input())

    # Get edit to do
    print(csvUtils.getRow(hotend, 'hotendID', hotendID))
    print("Do you want to edit company(1), size(2), material(3), or state(4)")
    editType = int(input())
    print("\nWhat would you like to change it to")
    newValue = input()

    # Save edit
    match editType:
        case 1:
            column = 'company'
        case 2:
            column = 'size'
        case 3:
            column = 'material'
        case 4:
            column = 'state'
        
    hotend = csvUtils.changeCell(hotend, 'hotendID', hotendID, column, newValue)
    csvUtils.writeData([hotendPath], [hotend])

def updateHotendMaintenance(hotend, maintenance, maintenancePath):
    # Get hotend for maintenance
    print(hotend)
    print('\nEnter ID of hotend for maintenance event')
    hotendID = int(input())

    # Get maintenance event
    print('What is the maintenance event, hotend cleaning(1)')
    eventType = int(input())
    match eventType:
        case 1:
            eventType = 'Hotend cleaned'
    
    print("What is the date of maintenance")
    date = input()

    # Save to file
    maintenance = csvUtils.addRow([len(maintenance),hotendID,date,eventType], maintenance)
    csvUtils.writeData([maintenancePath], [maintenance])

def readBuildplate(buildplatePath, buildplateMaintenancePath):
    # Read csv files
    buildplate, buildplateMaintenance = csvUtils.readData([buildplatePath, buildplateMaintenancePath])

    # Print information
    print('Buildplates:')
    print(buildplate.to_string(index=False))
    print('\n\nBuildplate maintenance history')
    print(buildplateMaintenance.to_string(index=False))

    # Update
    print('Would you like to edit a buildplate(1), create maintenance event(2), or return to home page(3)')
    action = int(input())

    match action:
        case 1:
            editBuildplate(buildplate, buildplatePath)
        case 2:
            updateBuildplateMaintanence(buildplate, buildplateMaintenance, buildplateMaintenancePath)
        case 3:
            print('Returning to home page')

def addBuildplate(buildplate, buildplatePath, purchases, purchasesPath, purchaseID):
    # Get buildplate to add
    print('What company is the buildplate from')
    buildplateCompany = input()
    print('What type of build plate is it')
    buildplateType = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    purchaseDate = input()
    print('What is the date arrived')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Add to csv files
    buildplate = csvUtils.addRow([len(buildplate),buildplateCompany,buildplateType], buildplate)
    purchases = csvUtils.addRow([purchaseID,'Buildplate',seller,len(buildplate)-1,purchaseDate, arrivalDate, cost], purchases)
    csvUtils.writeData([buildplatePath, purchasesPath], [buildplate, purchases])

def editBuildplate(buildplate, buildplatePath):
    # Get buildplate to edit
    print(buildplate.to_string(index=False))
    print('Enter ID for buildplate to edit')
    buildplateID = int(input())

    # Get column to edit
    print('Do you want to edit company(1), or type(2)')
    editType = int(input())
    print('What do you want to change that to')
    newValue = input()
    match editType:
        case 1:
            column = 'company'
        case 2:
            column = 'type'
    
    # Do edit
    buildplate = csvUtils.changeCell(buildplate, 'buildplateID', buildplateID, column, newValue)
    csvUtils.writeData([buildplatePath], [buildplate])

def updateBuildplateMaintanence(buildplate, maintenance, maintenancePath):
    # Get buildplate id
    print(buildplate.to_string(index=False))
    print('Enter ID of buildplate to edit')
    buildplateID = int(input())

    # Get maintenance type
    print('What is the maintenance event, buildplate cleaned(1)')
    eventType = int(input())
    match eventType:
        case 1:
            eventType = 'Buildplate Cleaned'
    
    print('What day was maintenance done')
    date = input()
    
    # Save update
    maintenance = csvUtils.addRow([len(maintenance),buildplateID,date,eventType], maintenance)
    csvUtils.writeData([maintenancePath], [maintenance])

def readAMS(amsPath, amsMaintenancePath):
    # Get dataframes
    ams, amsMaintenance = csvUtils.readData([amsPath, amsMaintenancePath])

    # Print data
    print('AMS')
    print(ams.to_string(index=False))
    print('\n\nAMS maintenance')
    print(amsMaintenance.to_string(index=False))

    # Get action
    print('Would you like to edit an AMS(1), add a maintenance event(2), or return to home page(3)')
    action = int(input())

    match action:
        case 1:
            editAMS(ams, amsPath)
        case 2:
            updateAMSMaintenance(ams, amsMaintenance, amsMaintenancePath)
        case 3:
            print('Returning to home page')

def addAMS(ams, amsPath, purchases, purchasesPath, purchaseID):
    # Get AMS to add
    print('What AMS model is added')
    amsModel = input()
    print('Where was it purchased from')
    seller = input()
    print('What date was this purchased')
    purchaseDate = input()
    print('What date did the ams arrive')
    arrivalDate = input()
    print('What did the AMS cost')
    cost = input()

    # Update dataframes
    ams = csvUtils.addRow([len(ams),amsModel], ams)
    purchases = csvUtils.addRow([purchaseID,'AMS',seller,len(ams)-1,purchaseDate,arrivalDate,cost], purchases)
    csvUtils.writeData([amsPath, purchasesPath], [ams, purchases])

def editAMS(ams, amsPath):
    # Get ams to edit
    print(ams.to_string(index=False))
    print('Enter ID of AMS to edit model')
    amsID = int(input())

    # Get edited value
    print('What is the new AMS model')
    newValue = input()

    # Save
    ams = csvUtils.changeCell(ams, 'amsID', amsID, 'amsModel', newValue)

def updateAMSMaintenance(ams, maintenance, maintenancePath):
    # Get ams to update
    print(ams.to_string(index=False))
    print('Enter ID of AMS for maintenance event')
    amsID = int(input())

    # Get maintenance update
    print('What is the new maintenance event, desiccant changed(1) or firmware updated(2)')
    eventType = int(input())

    match eventType:
        case 1:
            eventType = 'Desiccant changed'
            firmwareVersion = None
        case 2:
            eventType = 'Firmware updated'
            print('What version was it updated to')
            firmwareVersion = input()
    
    print('What date did this happen')
    date = input()
    
    # Update
    maintenance = csvUtils.addRow([len(maintenance),amsID,date,eventType,firmwareVersion], maintenance)
    csvUtils.writeData([maintenancePath], [maintenance])

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

def addFilament(filament, filamentPath, purchases, purchasesPath, purchaseID):
    # Get information
    print('What is the new filament company')
    company = input()
    print('What is the new filament colour')
    colour = input()
    print('What is the new filament material')
    material = input()
    print('What is the new filament diameter')
    diameter = input()
    print('What is the new filament starting amount')
    startingAmount = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    datePurchased = input()
    print('What is the date arrived')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Update dataframes
    filament = csvUtils.addRow([len(filament),company,colour,material,diameter,startingAmount,startingAmount,'Waiting',None], filament)
    purchases = csvUtils.addRow([purchaseID,'Filament',seller,len(filament)-1,datePurchased,arrivalDate,cost], purchases)
    csvUtils.writeData([filamentPath, purchasesPath], [filament, purchases])

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

def readFilamentDryers(dryerPath, dryerEventsPath):
    # Get information
    dryers, dryerEvents = csvUtils.readData([dryerPath, dryerEventsPath])
    
    # Print information
    print('Filament dryers')
    print(dryers.to_string(index=False))
    print('\n\nFilament dryer usage history')
    print(dryerEvents.to_string(index=False))

    # Get action
    print('\n\nWould you like to edit a filament dryer(1), or return to home page(2)')
    action = int(input())

    match action:
        case 1:
            editDryer(dryers, dryerPath)
        case 2:
            print('Returning to home page')

def addDryer(dryers, dryerPath, purchases, purchasesPath, purchaseID):
    # Get information about dryer
    print('What is the company for the filament dryer')
    company = input()
    print('What is the model of filament dryer')
    model = input()
    print('What is the capacity of the dryer')
    capacity = input()
    print('What is the min temperature')
    minTemp = input()
    print('What is the max temp')
    maxTemp = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date of purchase')
    purchaseDate = input()
    print('What is the date of arrival')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Update information
    dryers = csvUtils.addRow([len(dryers),company,model,capacity,minTemp,maxTemp], dryers)
    purchases = csvUtils.addRow([purchaseID,'Filament Dryer',seller,len(dryers)-1,purchaseDate,arrivalDate,cost], purchases)
    csvUtils.writeData([dryerPath, purchasesPath], [dryers, purchases])

def editDryer(dryers, dryerPath):
    # Get dryer to edit
    print(dryers.to_string(index=False))
    print('Enter ID of filament dryer to edit')
    dryerID = int(input())

    # Get value to edit
    print('Would you like to edit the company(1), model(2), capacity(3), min temperature(4), or max temperature(5)')
    editType = int(input())
    print('What is the new value')
    newValue = input()

    match editType:
        case 1:
            column = 'company'
        case 2:
            column = 'model'
        case 3:
            column = 'capacity'
        case 4:
            column = 'minTemp'
        case 5:
            column = 'maxTemp'
    
    # Save change
    dryers = csvUtils.changeCell(dryers, 'dryerID', dryerID, column, newValue)
    csvUtils.writeData([dryerPath], [dryers])

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

def addSpool(spools, spoolPath, purchases, purchasePath, purchaseID):
    # Get information about purchase
    print('What is the type of spool')
    spoolType = input()
    print('What is the date purchased')
    datePurchased = input()
    print('What is the date arrived')
    dateArrived = input()
    print("What is the cost")
    cost = input()

    # Update information
    spools = csvUtils.addRow([len(spools),spoolType], spools)
    purchases = csvUtils.addRow([purchaseID,'Reusable spool','Bambu',len(spools)-1,datePurchased, dateArrived,cost], purchases)
    csvUtils.writeData([spoolPath, purchasePath], [spools, purchases])

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

def addParts(parts, partsPath, purchases, purchasesPath, purchaseID):
    # Get information about purchase
    print("What is the part type")
    partType = input()
    print('What is the part spec')
    partSpec = input()
    print("What amount was purchased")
    amountPurchased = input()
    print('What was the date purchased')
    datePurchased = input()
    print('What was the date arrived')
    dateArrived = input()
    print('What is the cost')
    cost = input()
    print("Where was it purchased")
    seller = input()

    # Add information to csv
    parts = csvUtils.addRow([len(parts),partType,partSpec,amountPurchased,amountPurchased], parts)
    purchases = csvUtils.addRow([purchaseID,'Parts',seller,len(parts)-1,datePurchased,dateArrived,cost], purchases)
    csvUtils.writeData([partsPath, purchasesPath], [parts, purchases])

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

def readProjects(projectsPath):
    # Get dataframe
    projects = csvUtils.readData([projectsPath])[0]

    # Print dataframe
    print(projects.to_string(index=False))

    # Get action
    print('Would you like to add a project(1), edit a project(2), or return to home page(3)')
    action = int(input())

    match action:
        case 1:
            addProject(projects, projectsPath)
        case 2:
            print(2)
        case 3:
            print('Returning to home page')

def addProject(projects, projectsPath):
    # Get information about new project
    print('What is the new project name')
    name = input()

    # Update information
    projects = csvUtils.addRow([len(projects),name], projects)
    csvUtils.writeData([projectsPath], [projects])

def viewPurchases(allPaths):
    # Read dataframe
    purchases = csvUtils.readData([allPaths[-1]])[0]

    # Print purchase history
    print(purchases.to_string(index=False))

    # Update
    print('Would you like to add a purchase(1), edit a purchase(2), or return to home(3)')
    action = int(input())

    match action:
        case 1:
            addPurchases(allPaths)
        case 2:
            print(2)
        case 3:
            print('Returning to home')

def addPurchases(allPaths):
    # Read dataframes
    printers, hotends, buildplates, ams, filament, dryers, spools, parts, purchases = csvUtils.readData(allPaths)

    if len(purchases) == 0:
        purchaseID = 0
    else:
        purchaseID = purchases.iloc[-1]['purchaseID'] + 1

    # Get purchases required
    print('How many printers were purchased')
    printersPurchased = int(input())
    print('How many hotends were purchased')
    hotendsPurchased = int(input())
    print('How many buildplates were purchased')
    buildplatesPurchased = int(input())
    print('How many AMS were purchased')
    amsPurchased = int(input())
    print('How many filament were purchased')
    filamentPurchased = int(input())
    print('How many filament dryers were purchased')
    dryersPurchased = int(input())
    print('How many spools were purchased')
    spoolsPurchased = int(input())
    print('How many parts were purchased')
    partsPurchased = int(input())

    i = 0
    while i < printersPurchased:
        addPrinter(printers, allPaths[0], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < hotendsPurchased:
        addHotend(hotends, allPaths[1], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < buildplatesPurchased:
        addBuildplate(buildplates, allPaths[2], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < amsPurchased:
        addAMS(ams, allPaths[3], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < filamentPurchased:
        addFilament(filament, allPaths[4], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < dryersPurchased:
        addDryer(dryers, allPaths[5], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < spoolsPurchased:
        addSpool(spools, allPaths[6], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < partsPurchased:
        addParts(parts, allPaths[7], purchases, allPaths[-1], purchaseID)
        i += 1