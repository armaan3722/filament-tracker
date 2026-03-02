# Import modules
import interfaceCopy as io

# Const variables
PRINTER_PATH = './dataCopy/printer.csv'
PRINTER_MAINTENANCE_PATH = './dataCopy/printerMaintenance.csv'

# Main loop
runLoop = True
while runLoop:
    # Start home screen
    print('Would you like to view printer information(1), view filament information(2), view filament storage information(3), view non printed parts information(4),\nview project information(5), view print history(6), update filament usage(7), or end program(8)')
    action = int(input())

    # Run function
    match action:
        case 1:
            print(1)
            io.readPrinter(PRINTER_PATH, PRINTER_MAINTENANCE_PATH)
        case 2:
            print(2)
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
            print('Ending program')
            runLoop = False