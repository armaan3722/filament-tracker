# Import modules
import interfaceCopy as io

# Const variables
PRINTER_PATH = './data/printer/printer.csv'
PRINTER_MAINTENANCE_PATH = './data/printer/printerMaintenance.csv'
HOTEND_PATH = './data/hotend/hotend.csv'
HOTEND_MAINTENANCE_PATH = './data/hotend/hotendMaintenance.csv'
BUILDPLATE_PATH = './data/buildplate/buildplate.csv'
BUILDPLATE_MAINTENANCE_PATH = './data/buildplate/buildplateMaintenance.csv'
AMS_PATH = './data/ams/ams.csv'
AMS_MAINTENANCE_PATH = './data/ams/amsMaintenance.csv'
FILAMENT_PATH = './data/filament/filament.csv'
FILAMENT_DRYER_PATH = './data/dryers/dryers.csv'
FILAMENT_DRYER_EVENTS_PATH = './data/dryers/dryerEvents.csv'
SPOOLS_PATH = './data/filament/spools.csv'
PARTS_PATH = './data/parts/parts.csv'
PURCHASES_PATH = './data/purchases/purchases.csv'

PROJECTS_PATH = './data/printCategorization/projects.csv'

ALL_PURCHASE_PATHS = [PRINTER_PATH, HOTEND_PATH, BUILDPLATE_PATH, AMS_PATH, FILAMENT_PATH, FILAMENT_DRYER_PATH, SPOOLS_PATH, PARTS_PATH, PURCHASES_PATH]

# Main loop
runLoop = True
while runLoop:
    # Start home screen
    print('Would you like to view printer information(1), hotend information(2), build plate information(3), AMS information(4), \nfilament information(5), filament dryer information(6), reusable spools information(7), \nfilament storage information(8), non printed parts information(9), project information(10), \nprint history(11), purchases(12), update filament usage(13), or end program(14)')
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
            io.readFilament(FILAMENT_PATH, FILAMENT_DRYER_PATH, FILAMENT_DRYER_EVENTS_PATH)
        case 6:
            io.readFilamentDryers(FILAMENT_DRYER_PATH, FILAMENT_DRYER_EVENTS_PATH)
        case 7:
            io.readSpools(SPOOLS_PATH)
        case 8:
            print(8)
        case 9:
            io.readParts(PARTS_PATH)
        case 10:
            io.readProjects(PROJECTS_PATH)
        case 11:
            print(11)
        case 12:
            io.viewPurchases(ALL_PURCHASE_PATHS)
        case 13:
            print(13)
        case 14:
            print('Ending program')
            runLoop = False