# Import modules
import interfaceCopy as io

# Const variables
PRINTER_PATH = './dataCopy/printer.csv'
PRINTER_MAINTENANCE_PATH = './dataCopy/printerMaintenance.csv'
HOTEND_PATH = './dataCopy/hotend.csv'
HOTEND_MAINTENANCE_PATH = './dataCopy/hotendMaintenance.csv'
PURCHASES_PATH = './dataCopy/purchases.csv'

# Main loop
runLoop = True
while runLoop:
    # Start home screen
    print('Would you like to view printer information(1), view hotend information(2), view build plate information(3), view AMS information(4), \nview filament information(5), view filament storage information(6), view non printed parts information(7),\nview project information(8), view print history(9), update filament usage(10), or end program(11)')
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
            print(10)
        case 11:
            print('Ending program')
            runLoop = False