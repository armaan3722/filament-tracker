import csvUtils as csvUtils
import pandas as pd

def viewPurchases(allPaths):
    # Read dataframe
    purchases = csvUtils.readData([allPaths[-1]])[0]

    # Print purchase history
    print(purchases.to_string(index=False))

    # Update
    print('Would you like to add a purchase(1), edit a purchase(2), or return to home(3)')
    action = int(input())

    match action:
        case 1:
            addPurchases(allPaths)
        case 2:
            print(2)
        case 3:
            print('Returning to home')

def addPurchases(allPaths):
    # Read dataframes
    printers, hotends, buildplates, ams, filament, dryers, spools, parts, purchases = csvUtils.readData(allPaths)

    if len(purchases) == 0:
        purchaseID = 0
    else:
        purchaseID = purchases.iloc[-1]['purchaseID'] + 1

    # Get purchases required
    print('How many printers were purchased')
    printersPurchased = int(input())
    print('How many hotends were purchased')
    hotendsPurchased = int(input())
    print('How many buildplates were purchased')
    buildplatesPurchased = int(input())
    print('How many AMS were purchased')
    amsPurchased = int(input())
    print('How many filament were purchased')
    filamentPurchased = int(input())
    print('How many filament dryers were purchased')
    dryersPurchased = int(input())
    print('How many spools were purchased')
    spoolsPurchased = int(input())
    print('How many parts were purchased')
    partsPurchased = int(input())

    i = 0
    while i < printersPurchased:
        addPrinter(printers, allPaths[0], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < hotendsPurchased:
        addHotend(hotends, allPaths[1], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < buildplatesPurchased:
        addBuildplate(buildplates, allPaths[2], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < amsPurchased:
        addAMS(ams, allPaths[3], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < filamentPurchased:
        addFilament(filament, allPaths[4], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < dryersPurchased:
        addDryer(dryers, allPaths[5], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < spoolsPurchased:
        addSpool(spools, allPaths[6], purchases, allPaths[-1], purchaseID)
        i += 1
    
    i = 0
    while i < partsPurchased:
        addParts(parts, allPaths[7], purchases, allPaths[-1], purchaseID)
        i += 1

def addPrinter(printer, path, purchases, purchasesPath, purchaseID):
    # Get new printer information
    print('What is the new printer company')
    newPrinterCompany = input()
    print('What is the new printer model')
    newPrinterModel = input()
    print('What is the new printer name')
    newPrinterName = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the new printer cost')
    newPrinterCost = input()
    print('What is the new printer date purchased')
    newPrinterDate = input()
    print('What is the new printer date arrived')
    newPrinterArrivalDate = input()

    # Update dataframes
    printer = csvUtils.addRow([len(printer),newPrinterName,newPrinterCompany,newPrinterModel,0,0], printer)
    purchases = csvUtils.addRow([purchaseID,'Printer',seller,len(printer)-1,newPrinterDate,newPrinterArrivalDate,newPrinterCost], purchases)

    # Save
    csvUtils.writeData([path, purchasesPath], [printer, purchases])

def addHotend(hotend, hotendPath, purchases, purchasesPath, purchaseID):
    # Get hotend to add
    print('What is the new hotend company')
    newHotendCompany = input()
    print('What is the new hotend size')
    newHotendSize = input()
    print('What is the new hotend material')
    newHotendMaterial = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    newHotendDate = input()
    print('What is the date arrived')
    newHotendArrivalDate = input()
    print('What is the new hotend cost')
    newHotendCost = input()

    # Update dataframes
    hotend = csvUtils.addRow([len(hotend),newHotendCompany,newHotendSize,newHotendMaterial,'Passive'], hotend)
    purchases = csvUtils.addRow([purchaseID,'Hotend',seller,len(hotend)-1,newHotendDate,newHotendArrivalDate,newHotendCost], purchases)
    csvUtils.writeData([hotendPath, purchasesPath], [hotend, purchases])

def addBuildplate(buildplate, buildplatePath, purchases, purchasesPath, purchaseID):
    # Get buildplate to add
    print('What company is the buildplate from')
    buildplateCompany = input()
    print('What type of build plate is it')
    buildplateType = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    purchaseDate = input()
    print('What is the date arrived')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Add to csv files
    buildplate = csvUtils.addRow([len(buildplate),buildplateCompany,buildplateType], buildplate)
    purchases = csvUtils.addRow([purchaseID,'Buildplate',seller,len(buildplate)-1,purchaseDate, arrivalDate, cost], purchases)
    csvUtils.writeData([buildplatePath, purchasesPath], [buildplate, purchases])


def addAMS(ams, amsPath, purchases, purchasesPath, purchaseID):
    # Get AMS to add
    print('What AMS model is added')
    amsModel = input()
    print('Where was it purchased from')
    seller = input()
    print('What date was this purchased')
    purchaseDate = input()
    print('What date did the ams arrive')
    arrivalDate = input()
    print('What did the AMS cost')
    cost = input()

    # Update dataframes
    ams = csvUtils.addRow([len(ams),amsModel], ams)
    purchases = csvUtils.addRow([purchaseID,'AMS',seller,len(ams)-1,purchaseDate,arrivalDate,cost], purchases)
    csvUtils.writeData([amsPath, purchasesPath], [ams, purchases])

def addFilament(filament, filamentPath, purchases, purchasesPath, purchaseID):
    # Get information
    print('What is the new filament company')
    company = input()
    print('What is the new filament colour')
    colour = input()
    print('What is the new filament material')
    material = input()
    print('What is the new filament diameter')
    diameter = input()
    print('What is the new filament starting amount')
    startingAmount = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date purchased')
    datePurchased = input()
    print('What is the date arrived')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Update dataframes
    filament = csvUtils.addRow([len(filament),company,colour,material,diameter,startingAmount,startingAmount,'Waiting',None], filament)
    purchases = csvUtils.addRow([purchaseID,'Filament',seller,len(filament)-1,datePurchased,arrivalDate,cost], purchases)
    csvUtils.writeData([filamentPath, purchasesPath], [filament, purchases])

def addDryer(dryers, dryerPath, purchases, purchasesPath, purchaseID):
    # Get information about dryer
    print('What is the company for the filament dryer')
    company = input()
    print('What is the model of filament dryer')
    model = input()
    print('What is the capacity of the dryer')
    capacity = input()
    print('What is the min temperature')
    minTemp = input()
    print('What is the max temp')
    maxTemp = input()
    print('Where was it purchased from')
    seller = input()
    print('What is the date of purchase')
    purchaseDate = input()
    print('What is the date of arrival')
    arrivalDate = input()
    print('What is the cost')
    cost = input()

    # Update information
    dryers = csvUtils.addRow([len(dryers),company,model,capacity,minTemp,maxTemp], dryers)
    purchases = csvUtils.addRow([purchaseID,'Filament Dryer',seller,len(dryers)-1,purchaseDate,arrivalDate,cost], purchases)
    csvUtils.writeData([dryerPath, purchasesPath], [dryers, purchases])


def addSpool(spools, spoolPath, purchases, purchasePath, purchaseID):
    # Get information about purchase
    print('What is the type of spool')
    spoolType = input()
    print('What is the date purchased')
    datePurchased = input()
    print('What is the date arrived')
    dateArrived = input()
    print("What is the cost")
    cost = input()

    # Update information
    spools = csvUtils.addRow([len(spools),spoolType], spools)
    purchases = csvUtils.addRow([purchaseID,'Reusable spool','Bambu',len(spools)-1,datePurchased, dateArrived,cost], purchases)
    csvUtils.writeData([spoolPath, purchasePath], [spools, purchases])

def addParts(parts, partsPath, purchases, purchasesPath, purchaseID):
    # Get information about purchase
    print("What is the part type")
    partType = input()
    print('What is the part spec')
    partSpec = input()
    print("What amount was purchased")
    amountPurchased = input()
    print('What was the date purchased')
    datePurchased = input()
    print('What was the date arrived')
    dateArrived = input()
    print('What is the cost')
    cost = input()
    print("Where was it purchased")
    seller = input()

    # Add information to csv
    parts = csvUtils.addRow([len(parts),partType,partSpec,amountPurchased,amountPurchased], parts)
    purchases = csvUtils.addRow([purchaseID,'Parts',seller,len(parts)-1,datePurchased,dateArrived,cost], purchases)
    csvUtils.writeData([partsPath, purchasesPath], [parts, purchases])