# Import modules
import equipment as equipment
import materials as materials
import projects as projects
import purchase as purchase
import usage as usage

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
CATEGORIES_PATH = './data/printCategorization/categories.csv'
COLLECTIONS_PATH = './data/printCategorization/collections.csv'
PRINT_JOBS_PATH = './data/usage/printJobs.csv'
FILAMENT_USED_PATH = './data/usage/filamentUsed.csv'
PLATE_CONFIG_PATH = './data/printConfigs/plateConfigs.csv'
FILAMENT_CONFIG_PATH = './data/printConfigs/filamentConfigs.csv'

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
            equipment.readPrinter(PRINTER_PATH, PRINTER_MAINTENANCE_PATH)
        case 2:
            equipment.readHotend(HOTEND_PATH, HOTEND_MAINTENANCE_PATH)
        case 3:
            equipment.readBuildplate(BUILDPLATE_PATH, BUILDPLATE_MAINTENANCE_PATH)
        case 4:
            equipment.readAMS(AMS_PATH, AMS_MAINTENANCE_PATH)
        case 5:
            materials.readFilament(FILAMENT_PATH, FILAMENT_DRYER_PATH, FILAMENT_DRYER_EVENTS_PATH)
        case 6:
            materials.readFilamentDryers(FILAMENT_DRYER_PATH, FILAMENT_DRYER_EVENTS_PATH)
        case 7:
            materials.readSpools(SPOOLS_PATH)
        case 8:
            print(8)
        case 9:
            materials.readParts(PARTS_PATH)
        case 10:
            projects.readProjects(PROJECTS_PATH, CATEGORIES_PATH)
        case 11:
            print(11)
        case 12:
            purchase.viewPurchases(ALL_PURCHASE_PATHS)
        case 13:
            usage.addFilamentUsage(PROJECTS_PATH, CATEGORIES_PATH, COLLECTIONS_PATH, PRINT_JOBS_PATH, PRINTER_PATH, AMS_PATH, HOTEND_PATH, BUILDPLATE_PATH, FILAMENT_PATH, FILAMENT_USED_PATH)
        case 14:
            print('Ending program')
            runLoop = False