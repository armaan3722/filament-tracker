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
    print('What is the new printer cost')
    newPrinterCost = input()
    print('What is the new printer date purchased')
    newPrinterDate = input()
    print('What is the new printer date arrived')
    newPrinterArrivalDate = input()

    # Update dataframes
    printer = csvUtils.addRow([len(printer),newPrinterName,newPrinterCompany,newPrinterModel,0], printer)
    purchases = csvUtils.addRow([purchaseID,'Printer',len(printer)-1,newPrinterDate,newPrinterArrivalDate,newPrinterCost], purchases)

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
    match eventType:
        case 1:
            eventType = 'Automatic Calibration'
        case 2:
            eventType = 'Firmware Update'

    # Get date
    print('What date did this maintenance event happen')
    eventDate = input()
        
    # Save to file
    maintenance = csvUtils.addRow([len(maintenance),printerID,eventDate,eventType],maintenance)
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
    print('What is the date purchased')
    newHotendDate = input()
    print('What is the date arrived')
    newHotendArrivalDate = input()
    print('What is the new hotend cost')
    newHotendCost = input()

    # Update dataframes
    hotend = csvUtils.addRow([len(hotend),newHotendCompany,newHotendSize,newHotendMaterial,'Passive'], hotend)
    purchases = csvUtils.addRow([purchaseID,'Hotend',len(hotend)-1,newHotendDate,newHotendArrivalDate,newHotendCost], purchases)
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
    action = input()

    match action:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            print('Returning to home page')

def addBuildplate(buildplate, buildplatePath, purchases, purchasesPath, purchaseID):
    # Get buildplate to add
    print('What company is the buildplate from')
    buildplateCompany = input()
    print('What type of build plate is it')
    buildplateType = input()
    print('What is the date purchased')
    purchaseDate = input()
    print('What is the date arrived')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Add to csv files
    buildplate = csvUtils.addRow([len(buildplate),buildplateCompany,buildplateType], buildplate)
    purchases = csvUtils.addRow([purchaseID,'Buildplate',len(buildplate)-1,purchaseDate, arrivalDate, cost], purchases)
    csvUtils.writeData([buildplatePath, purchasesPath], [buildplate, purchases])

def viewPurchases(allPaths):
    # Read dataframe
    purchases = csvUtils.readData([allPaths[3]])[0]

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
    printers, hotends, buildplates, purchases = csvUtils.readData(allPaths)
    purchaseID = len(purchases)

    # Get purchases required
    print('How many printers were purchased')
    printersPurchased = int(input())
    # print('How many AMS were purchased')
    # amsPurchased = int(input())
    print('How many hotends were purchased')
    hotendsPurchased = int(input())
    print('How many buildplates were purchased')
    buildplatesPurchased = int(input())
    # print('How many rolls of filament were purchased')
    # filamentPurchased = int(input())

    i = 0
    while i < printersPurchased:
        addPrinter(printers, allPaths[0], purchases, allPaths[3], purchaseID)
        i += 1
    
    i = 0
    while i < hotendsPurchased:
        addHotend(hotends, allPaths[1], purchases, allPaths[3], purchaseID)
        i += 1
    
    i = 0
    while i < buildplatesPurchased:
        addBuildplate(buildplates, allPaths[2], purchases, allPaths[3], purchaseID)
        i += 1