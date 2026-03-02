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
    print('\n\nPrinter maintenance history')
    print(printerMaintenance.to_string(index=False))

    # Update
    print('\n\nWould you like to add a printer(1), edit printer information(2), create maintenance event(3), or go back to home page(4)')
    action = int(input())

    match action:
        case 1:
            addPrinter(printer, printerPath)
        case 2:
            editPrinter(printer, printerPath)
        case 3:
            updateMaintenance(printer, printerMaintenance, printerMaintenancePath)
        case 4:
            print('Returning to home page')

def addPrinter(printer, path):
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

    # Update dataframe
    printer = csvUtils.addRow([len(printer),newPrinterName,newPrinterCompany,newPrinterModel,newPrinterDate,newPrinterCost,0], printer)

    # Save
    csvUtils.writeData([path], [printer])

def editPrinter(printer, path):
    # Get printer to edit
    print(printer.to_string(index=False))
    print('\nEnter ID of printer to edit')
    printerID = int(input())

    # Get what to edit
    print(csvUtils.getRow(printer, 'printerID', printerID))
    print('Do you want to edit the name(1), company(2), model(3), date purchased(4), or cost(5)')
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
        case 4:
            column = 'printerDatePurchased'
        case 5:
            column = 'printerCost'
    
    printer = csvUtils.changeCell(printer, 'printerID', printerID, column, newValue)
    csvUtils.writeData([path], [printer])

def updateMaintenance(printer, maintenance, maintenancePath):
    # Get printer for event
    print(printer)
    print('\nEnter ID of printer for maintenance event')
    printerID = int(input())

    # Get event type
    print('Which event was done, maintenance(1), replacement(2), or upgrade(3)')
    eventType = int(input())

    # Get operation done
    match eventType:
        case 1:
            # Maintenance event
            print('What was done, hotend cleaned(1), build plate cleaned(2), printer recalibrated(3)')
            action = int(input())
            match action:
                case 1:
                    action = 'Hotend Cleaned'
                case 2:
                    action = 'Build Plate Cleaned'
                case 3:
                    action = 'Printer Recalibrated'
        case 2:
            #Replacement event
            print('What was replaced, hotend(1), or build plate(2)')
            action = int(input())
            match action:
                case 1:
                    action = 'Hotend replaced'
                case 2:
                    action = 'Build plate replaced'
        case 3:
            #Upgrade event
            print('What was upgraded, hotend(1), build plate(2), or AMS(3)')
            action = int(input())
            match action:
                case 1:
                    action = 'Hotend upgraded'
                case 2:
                    action = 'Build plate upgraded'
                case 3:
                    action = 'AMS upgraded'
    match eventType:
        case 1:
            eventType = 'Maintenance'
        case 2:
            eventType = 'Replacement'
        case 3:
            eventType = 'Upgrade'

    # Get date
    print('What date did this happen')
    eventDate = input()
        
    # Save to file
    maintenance = csvUtils.addRow([len(maintenance),printerID,eventDate,eventType,action],maintenance)
    csvUtils.writeData([maintenancePath], [maintenance])