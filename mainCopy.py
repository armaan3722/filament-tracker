# Import modules
import interfaceCopy as io

# Const variables
PRINTER_PATH = './dataCopy/printer.csv'
PRINTER_MAINTENANCE_PATH = './dataCopy/printerMaintenance.csv'
HOTEND_PATH = './dataCopy/hotend.csv'
HOTEND_MAINTENANCE_PATH = './dataCopy/hotendMaintenance.csv'
PURCHASES_PATH = './dataCopy/purchases.csv'

ALL_PURCHASE_PATHS = [PRINTER_PATH, HOTEND_PATH, PURCHASES_PATH]

# Main loop
runLoop = True
while runLoop:
    # Start home screen
    print('Would you like to view printer information(1), hotend information(2), build plate information(3), AMS information(4), \nfilament information(5), filament storage information(6), non printed parts information(7),project information(8), \nprint history(9), add a purchase(10), update filament usage(11), or end program(12)')
    action = int(input())

    # Run function
    match action:
        case 1:
            io.readPrinter(PRINTER_PATH, PRINTER_MAINTENANCE_PATH, PURCHASES_PATH)
        case 2:
            io.readHotend(HOTEND_PATH, HOTEND_MAINTENANCE_PATH, PURCHASES_PATH)
        case 3:
            print(3)
        case 4:
            print(4)
        case 5:
            print(5)
        case 6:
            print(6)
        case 7:
            print(7)
        case 8:
            print(8)
        case 9:
            print(9)
        case 10:
            io.addPurchases(ALL_PURCHASE_PATHS)
        case 11:
            print(11)
        case 12:
            print('Ending program')
            runLoop = False