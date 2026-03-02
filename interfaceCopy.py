# Import modules
import data as csvUtils

# Get printer information
def readPrinter(printerPath, printerMaintenancePath):
    # Get csv files
    printer, printerMaintenance = csvUtils.readData([printerPath, printerMaintenancePath])

    # Print dataframes
    print("Printers:")
    print(printer)
    print('\n\nPrinter maintenance history')
    print(printerMaintenance)

    # Update
    print('\n\nWould you like to add a printer(1), edit printer information(2), create maintenance event(3), or go back to home page(4)')
    action = int(input())

    match action:
        case 1:
            addPrinter(printer, printerPath)
        case 2:
            print(2)
        case 3:
            print(3)
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