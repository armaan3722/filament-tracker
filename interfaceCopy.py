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