from filament_tracker import csv_utils


# FILAMENT
def read_filament(filament_path, dryer_path, dryer_events_path):
    # Get filament information
    filament, dryers, dryer_events = csv_utils.read_data(
        [filament_path, dryer_path, dryer_events_path]
    )

    # Print data
    print("Filament")
    print(filament.to_string(index=False))

    # Get action
    print(
        "\n\nWould you like to edit filament(1), add a drying event(2), or return to home(3)"
    )
    action = int(input())

    match action:
        case 1:
            edit_filament(filament, filament_path)
        case 2:
            add_drying_event(
                filament, filament_path, dryers, dryer_events, dryer_events_path
            )
        case 3:
            print("Returning to home page")


def edit_filament(filament, filament_path):
    # Get filament to edit
    print(filament.to_string(index=False))
    print("Enter ID of filament to edit")
    filament_id = int(input())

    # Get value to edit
    print(
        "Do you want to edit company(1), colour(2), material(3), diameter(4), starting amount(5), or state(6)"
    )
    edit_type = int(input())
    print("Enter new value")
    new_value = input()

    match edit_type:
        case 1:
            column = "filament_company"
        case 2:
            column = "filament_colour"
        case 3:
            column = "filament_material"
        case 4:
            column = "diameter"
        case 5:
            column = "starting_amount"
        case 6:
            column = "state"

    # Edit
    filament = csv_utils.change_cell(
        filament, "filament_id", filament_id, column, new_value
    )
    csv_utils.write_data([filament_path], [filament])


def add_drying_event(filament, filament_path, dryers, dryer_events, dryer_events_path):
    # Get filament roll dried
    print(filament.to_string(index=False))
    print("Enter ID of filament roll dried")
    filament_id = int(input())

    # Get dryer used
    print(dryers.to_string(index=False))
    print("Enter ID of filament dryer used")
    dryer_id = int(input())

    # Get drying information
    print("How long was the filament dried")
    length = input()
    print("What temperature was the filament dried at")
    temp = input()
    print("When was the filament dried")
    date = input()

    # Reformat
    filament["date_last_dried"] = filament["date_last_dried"].astype(str)

    # Save to csv files
    filament = csv_utils.change_cell(
        filament, "filament_id", filament_id, "date_last_dried", date
    )
    dryer_events = csv_utils.add_row(
        [len(dryer_events), filament_id, dryer_id, temp, length, date], dryer_events
    )
    csv_utils.write_data([filament_path, dryer_events_path], [filament, dryer_events])


# REUSABLE SPOOLS
def read_spools(spool_path):
    # Convert to csv
    spools = csv_utils.read_data([spool_path])[0]

    # Print spool information
    print("Reusable spools")
    print(spools.to_string(index=False))

    # Get action
    print("\n\nWould you like to edit a spool(1) or return to home page(2)")
    action = int(input())

    match action:
        case 1:
            edit_spool(spools, spool_path)
        case 2:
            print("Returning to home page")


def edit_spool(spools, spool_path):
    # Get spool to edit
    print("Enter ID of spool to edit")
    spool_id = int(input())

    # Get column to edit
    print("What would you like to set the type to")
    new_value = input()

    # Modify
    spools = csv_utils.change_cell(spools, "spool_id", spool_id, "type", new_value)
    csv_utils.write_data([spool_path], [spools])


# PARTS
def read_parts(parts_path):
    # Get information from csv
    parts = csv_utils.read_data([parts_path])[0]

    # Print information
    print("Other parts information")
    print(parts.to_string(index=False))

    # Get next action
    print("Would you like to edit a part(1), or return to home page(2)")
    action = int(input())

    match action:
        case 1:
            edit_parts(parts, parts_path)
        case 2:
            print("Returning to home page")


def edit_parts(parts, parts_path):
    # Get ID of part to edit
    print(parts.to_string(index=False))
    print("Enter ID of part to edit")
    part_id = int(input())

    # Get what to edit
    print("Would you like to edit the type(1), spec(2), or starting quantity(3)")
    edit_type = int(input())
    print("What is the new value")
    new_value = input()

    match edit_type:
        case 1:
            column = "part_type"
        case 2:
            column = "part_spec"
        case 3:
            column = "starting_amount"

    # Save change
    parts = csv_utils.change_cell(parts, "part_id", part_id, column, new_value)
    csv_utils.write_data([parts_path], [parts])
