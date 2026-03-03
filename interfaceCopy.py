# Import modules
import data as csvUtils
import pandas as pd

# Get printer information
def readPrinter(printerPath, printerMaintenancePath, purchasesPath):
    # Get csv files
    printer, printerMaintenance, purchases = csvUtils.readData([printerPath, printerMaintenancePath, purchasesPath])

    # Print dataframes
    print("Printers:")
    print(printer.to_string(index=False))
    print('\n\nPrinter maintenance history:')
    print(printerMaintenance.to_string(index=False))

    # Update
    print('\n\nWould you like to add a printer(1), edit printer information(2), create maintenance event(3), or go back to home page(4)')
    action = int(input())

    match action:
        case 1:
            addPrinter(printer, printerPath, purchases, purchasesPath)
        case 2:
            editPrinter(printer, printerPath)
        case 3:
            updateMaintenance(printer, printerMaintenance, printerMaintenancePath)
        case 4:
            print('Returning to home page')

def addPrinter(printer, path, purchases, purchasesPath):
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
    purchases = csvUtils.addRow([len(purchases),'printer',len(printer)-1,newPrinterDate,newPrinterArrivalDate,newPrinterCost], purchases)

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

def updateMaintenance(printer, maintenance, maintenancePath):
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

def readHotend(hotendPath, hotendMaintenancePath, purchasesPath):
    # Read csv files
    hotend, hotendMaintenance, purchases = csvUtils.readData([hotendPath, hotendMaintenancePath, purchasesPath])

    # Print information
    print('Hotends:')
    print(hotend.to_string(index=False))
    print('\n\nHotend maintenance history:')
    print(hotendMaintenance.to_string(index=False))

    # Update
    print('\n\nWould you like to add a hotend(1), edit a hotend(2), create a maintenance event(3), or return to home(4)')
    action = int(input())

    match action:
        case 1:
            addHotend(hotend, hotendPath, purchases, purchasesPath)
        case 2:
            print(2)
        case 3:
            print(3)
        case 4:
            print('Returning to home page')

def addHotend(hotend, hotendPath, purchases, purchasesPath):
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
    hotend = csvUtils.addRow([len(hotend),newHotendCompany,newHotendSize,newHotendMaterial], hotend)
    purchases = csvUtils.addRow([len(purchases),'Hotend',len(hotend)-1,newHotendDate,newHotendArrivalDate,newHotendCost], purchases)
    csvUtils.writeData([hotendPath, purchasesPath], [hotend, purchases])