from filament_tracker import csv_utils


# PRINTER
def read_printer(printer_path, printer_maintenance_path):
    # Get csv files
    printer, printer_maintenance = csv_utils.read_data(
        [printer_path, printer_maintenance_path]
    )

    # Print dataframes
    print("Printers:")
    print(printer.to_string(index=False))
    print("\n\nPrinter maintenance history:")
    print(printer_maintenance.to_string(index=False))

    # Update
    print(
        "\n\nWould you like to edit a printer(1), create maintenance event(2), or go back to home page(3)"
    )
    action = int(input())

    match action:
        case 1:
            edit_printer(printer, printer_path)
        case 2:
            update_printer_maintenance(
                printer, printer_maintenance, printer_maintenance_path
            )
        case 3:
            print("Returning to home page")


def edit_printer(printer, path):
    # Get printer to edit
    print(printer.to_string(index=False))
    print("\nEnter ID of printer to edit")
    printer_id = int(input())

    # Get what to edit
    print(csv_utils.get_row(printer, "printerID", printer_id))
    print("Do you want to edit the name(1), company(2), or model(3)")
    edit_type = int(input())
    print("What is the new value")
    new_value = input()

    # Save edit
    match edit_type:
        case 1:
            column = "printerName"
        case 2:
            column = "printerCompany"
        case 3:
            column = "printerModel"

    printer = csv_utils.change_cell(printer, "printerID", printer_id, column, new_value)
    csv_utils.write_data([path], [printer])


def update_printer_maintenance(printer, maintenance, maintenance_path):
    # Get printer for maintenance
    print(printer.to_string(index=False))
    print("\nEnter ID of printer for maintenance event")
    printer_id = int(input())

    # Get maintenance type
    print("Which maintenance was done, automatic calibration(1) or firmware update(2)")
    event_type = int(input())

    firmware_version = None
    match event_type:
        case 1:
            event_type = "Automatic Calibration"
        case 2:
            event_type = "Firmware Update"
            print("What version was it updated to")
            firmware_version = input()

    # Get date
    print("What date did this maintenance event happen")
    event_date = input()

    # Save to file
    maintenance = csv_utils.add_row(
        [len(maintenance), printer_id, event_date, event_type, firmware_version],
        maintenance,
    )
    csv_utils.write_data([maintenance_path], [maintenance])


# HOTEND
def read_hotend(hotend_path, hotend_maintenance_path):
    # Read csv files
    hotend, hotend_maintenance = csv_utils.read_data(
        [hotend_path, hotend_maintenance_path]
    )

    # Print information
    print("Hotends:")
    print(hotend.to_string(index=False))
    print("\n\nHotend maintenance history:")
    print(hotend_maintenance.to_string(index=False))

    # Update
    print(
        "\n\nWould you like to edit a hotend(1), create a maintenance event(2), or return to home(3)"
    )
    action = int(input())

    match action:
        case 1:
            edit_hotend(hotend, hotend_path)
        case 2:
            update_hotend_maintenance(
                hotend, hotend_maintenance, hotend_maintenance_path
            )
        case 3:
            print("Returning to home page")


def edit_hotend(hotend, hotend_path):
    # Get hotend to edit
    print(hotend.to_string(index=False))
    print("\nEnter ID of hotend to edit")
    hotend_id = int(input())

    # Get edit to do
    print(csv_utils.get_row(hotend, "hotendID", hotend_id))
    print("Do you want to edit company(1), size(2), material(3), or state(4)")
    edit_type = int(input())
    print("\nWhat would you like to change it to")
    new_value = input()

    # Save edit
    match edit_type:
        case 1:
            column = "company"
        case 2:
            column = "size"
        case 3:
            column = "material"
        case 4:
            column = "state"

    hotend = csv_utils.change_cell(hotend, "hotendID", hotend_id, column, new_value)
    csv_utils.write_data([hotend_path], [hotend])


def update_hotend_maintenance(hotend, maintenance, maintenance_path):
    # Get hotend for maintenance
    print(hotend)
    print("\nEnter ID of hotend for maintenance event")
    hotend_id = int(input())

    # Get maintenance event
    print("What is the maintenance event, hotend cleaning(1)")
    event_type = int(input())
    match event_type:
        case 1:
            event_type = "Hotend cleaned"

    print("What is the date of maintenance")
    date = input()

    # Save to file
    maintenance = csv_utils.add_row(
        [len(maintenance), hotend_id, date, event_type], maintenance
    )
    csv_utils.write_data([maintenance_path], [maintenance])


# BUILDPLATE
def read_buildplate(buildplate_path, buildplate_maintenance_path):
    # Read csv files
    buildplate, buildplate_maintenance = csv_utils.read_data(
        [buildplate_path, buildplate_maintenance_path]
    )

    # Print information
    print("Buildplates:")
    print(buildplate.to_string(index=False))
    print("\n\nBuildplate maintenance history")
    print(buildplate_maintenance.to_string(index=False))

    # Update
    print(
        "Would you like to edit a buildplate(1), create maintenance event(2), or return to home page(3)"
    )
    action = int(input())

    match action:
        case 1:
            edit_buildplate(buildplate, buildplate_path)
        case 2:
            update_buildplate_maintenance(
                buildplate, buildplate_maintenance, buildplate_maintenance_path
            )
        case 3:
            print("Returning to home page")


def edit_buildplate(buildplate, buildplate_path):
    # Get buildplate to edit
    print(buildplate.to_string(index=False))
    print("Enter ID for buildplate to edit")
    buildplate_id = int(input())

    # Get column to edit
    print("Do you want to edit company(1), or type(2)")
    edit_type = int(input())
    print("What do you want to change that to")
    new_value = input()
    match edit_type:
        case 1:
            column = "company"
        case 2:
            column = "type"

    # Do edit
    buildplate = csv_utils.change_cell(
        buildplate, "buildplateID", buildplate_id, column, new_value
    )
    csv_utils.write_data([buildplate_path], [buildplate])


def update_buildplate_maintenance(buildplate, maintenance, maintenance_path):
    # Get buildplate id
    print(buildplate.to_string(index=False))
    print("Enter ID of buildplate to edit")
    buildplate_id = int(input())

    # Get maintenance type
    print("What is the maintenance event, buildplate cleaned(1)")
    event_type = int(input())
    match event_type:
        case 1:
            event_type = "Buildplate Cleaned"

    print("What day was maintenance done")
    date = input()

    # Save update
    maintenance = csv_utils.add_row(
        [len(maintenance), buildplate_id, date, event_type], maintenance
    )
    csv_utils.write_data([maintenance_path], [maintenance])


# AMS
def read_ams(ams_path, ams_maintenance_path):
    # Get dataframes
    ams, ams_maintenance = csv_utils.read_data([ams_path, ams_maintenance_path])

    # Print data
    print("AMS")
    print(ams.to_string(index=False))
    print("\n\nAMS maintenance")
    print(ams_maintenance.to_string(index=False))

    # Get action
    print(
        "Would you like to edit an AMS(1), add a maintenance event(2), or return to home page(3)"
    )
    action = int(input())

    match action:
        case 1:
            edit_ams(ams, ams_path)
        case 2:
            update_ams_maintenance(ams, ams_maintenance, ams_maintenance_path)
        case 3:
            print("Returning to home page")


def edit_ams(ams, ams_path):
    # Get ams to edit
    print(ams.to_string(index=False))
    print("Enter ID of AMS to edit model")
    ams_id = int(input())

    # Get edited value
    print("What is the new AMS model")
    new_value = input()

    # Save
    ams = csv_utils.change_cell(ams, "amsID", ams_id, "amsModel", new_value)


def update_ams_maintenance(ams, maintenance, maintenance_path):
    # Get ams to update
    print(ams.to_string(index=False))
    print("Enter ID of AMS for maintenance event")
    ams_id = int(input())

    # Get maintenance update
    print(
        "What is the new maintenance event, desiccant changed(1) or firmware updated(2)"
    )
    event_type = int(input())

    match event_type:
        case 1:
            event_type = "Desiccant changed"
            firmware_version = None
        case 2:
            event_type = "Firmware updated"
            print("What version was it updated to")
            firmware_version = input()

    print("What date did this happen")
    date = input()

    # Update
    maintenance = csv_utils.add_row(
        [len(maintenance), ams_id, date, event_type, firmware_version], maintenance
    )
    csv_utils.write_data([maintenance_path], [maintenance])


# DRYERS
def read_filament_dryers(dryer_path, dryer_events_path):
    # Get information
    dryers, dryer_events = csv_utils.read_data([dryer_path, dryer_events_path])

    # Print information
    print("Filament dryers")
    print(dryers.to_string(index=False))
    print("\n\nFilament dryer usage history")
    print(dryer_events.to_string(index=False))

    # Get action
    print("\n\nWould you like to edit a filament dryer(1), or return to home page(2)")
    action = int(input())

    match action:
        case 1:
            edit_dryer(dryers, dryer_path)
        case 2:
            print("Returning to home page")


def edit_dryer(dryers, dryer_path):
    # Get dryer to edit
    print(dryers.to_string(index=False))
    print("Enter ID of filament dryer to edit")
    dryer_id = int(input())

    # Get value to edit
    print(
        "Would you like to edit the company(1), model(2), capacity(3), min temperature(4), or max temperature(5)"
    )
    edit_type = int(input())
    print("What is the new value")
    new_value = input()

    match edit_type:
        case 1:
            column = "company"
        case 2:
            column = "model"
        case 3:
            column = "capacity"
        case 4:
            column = "minTemp"
        case 5:
            column = "maxTemp"

    # Save change
    dryers = csv_utils.change_cell(dryers, "dryerID", dryer_id, column, new_value)
    csv_utils.write_data([dryer_path], [dryers])
