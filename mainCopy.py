# Import modules
import interfaceCopy as io

# Const variables
PRINTER_PATH = './dataCopy/printer.csv'
PRINTER_MAINTENANCE_PATH = './dataCopy/printerMaintenance.csv'
HOTEND_PATH = './dataCopy/hotend.csv'
HOTEND_MAINTENANCE_PATH = './dataCopy/hotendMaintenance.csv'
BUILDPLATE_PATH = './dataCopy/buildplate.csv'
BUILDPLATE_MAINTENANCE_PATH = './dataCopy/buildplateMaintenance.csv'
AMS_PATH = './dataCopy/ams.csv'
AMS_MAINTENANCE_PATH = './dataCopy/amsMaintenance.csv'
FILAMENT_PATH = './dataCopy/filament.csv'
PURCHASES_PATH = './dataCopy/purchases.csv'

ALL_PURCHASE_PATHS = [PRINTER_PATH, HOTEND_PATH, BUILDPLATE_PATH, AMS_PATH, FILAMENT_PATH, PURCHASES_PATH]

# Main loop
runLoop = True
while runLoop:
    # Start home screen
    print('Would you like to view printer information(1), hotend information(2), build plate information(3), AMS information(4), \nfilament information(5), filament rolls information(6), filament storage information(7), non printed parts information(8), project information(9), \nprint history(10), purchases(11), update filament usage(12), or end program(13)')
    action = int(input())

    # Run function
    match action:
        case 1:
            io.readPrinter(PRINTER_PATH, PRINTER_MAINTENANCE_PATH)
        case 2:
            io.readHotend(HOTEND_PATH, HOTEND_MAINTENANCE_PATH)
        case 3:
            io.readBuildplate(BUILDPLATE_PATH, BUILDPLATE_MAINTENANCE_PATH)
        case 4:
            io.readAMS(AMS_PATH, AMS_MAINTENANCE_PATH)
        case 5:
            io.readFilament(FILAMENT_PATH)
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
            io.viewPurchases(ALL_PURCHASE_PATHS)
        case 12:
            print(11)
        case 13:
            print('Ending program')
            runLoop = False