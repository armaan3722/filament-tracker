import csvUtils as csvUtils
import pandas as pd

# PRINTER
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


# HOTEND
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


# BUILDPLATE
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


# AMS
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

# DRYERS
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