from pathlib import Path

import pandas as pd

from filament_tracker import csv_utils


# PRINTER
def read_printer(
    printer_path: str | Path, printer_maintenance_path: str | Path
) -> None:
    """Read printer data and maintenance history, then present a menu for updates.

    Reads the printer and printer maintenance CSV files, displays their contents,
    and prompts the user to edit a printer, create a maintenance event, or return
    to the home page.

    Args:
        printer_path: Path to the printer CSV file.
        printer_maintenance_path: Path to the printer maintenance history CSV file.
    """
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


def edit_printer(printer: pd.DataFrame, path: str | Path) -> None:
    """Edit a printer's name, company, or model.

    Displays all printers, prompts for a printer ID and the field to edit
    (name, company, or model), then saves the change to the CSV file.

    Args:
        printer: DataFrame containing printer data.
        path: Path to the printer CSV file.
    """
    # Get printer to edit
    print(printer.to_string(index=False))
    print("\nEnter ID of printer to edit")
    printer_id = int(input())

    # Get what to edit
    print(csv_utils.get_row(printer, "printer_id", printer_id))
    print("Do you want to edit the name(1), company(2), or model(3)")
    edit_type = int(input())
    print("What is the new value")
    new_value = input()

    # Save edit
    match edit_type:
        case 1:
            column = "printer_name"
        case 2:
            column = "printer_company"
        case 3:
            column = "printer_model"

    printer = csv_utils.change_cell(
        printer, "printer_id", printer_id, column, new_value
    )
    csv_utils.write_data([path], [printer])


def update_printer_maintenance(
    printer: pd.DataFrame, maintenance: pd.DataFrame, maintenance_path: str | Path
) -> None:
    """Create a maintenance event for a printer.

    Prompts for a printer ID, maintenance type (automatic calibration or firmware
    update), date, and optionally the firmware version. Appends the event to the
    maintenance history CSV file.

    Args:
        printer: DataFrame containing printer data.
        maintenance: DataFrame containing maintenance history.
        maintenance_path: Path to the maintenance history CSV file.
    """
    # Get printer for maintenance
    print(printer.to_string(index=False))
    print("\nEnter ID of printer for maintenance event")
    printer_id = int(input())

    # Get maintenance type
    print("Which maintenance was done, automatic calibration(1) or firmware update(2)")
    event_type = int(input())

    firmware_version: str | None = None
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
def read_hotend(hotend_path: str | Path, hotend_maintenance_path: str | Path) -> None:
    """Read hotend data and maintenance history, then present a menu for updates.

    Reads the hotend and hotend maintenance CSV files, displays their contents,
    and prompts the user to edit a hotend, create a maintenance event, or return
    to the home page.

    Args:
        hotend_path: Path to the hotend CSV file.
        hotend_maintenance_path: Path to the hotend maintenance history CSV file.
    """
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


def edit_hotend(hotend: pd.DataFrame, hotend_path: str | Path) -> None:
    """Edit a hotend's company, size, material, or state.

    Displays all hotends, prompts for a hotend ID and the field to edit,
    then saves the change to the CSV file.

    Args:
        hotend: DataFrame containing hotend data.
        hotend_path: Path to the hotend CSV file.
    """
    # Get hotend to edit
    print(hotend.to_string(index=False))
    print("\nEnter ID of hotend to edit")
    hotend_id = int(input())

    # Get edit to do
    print(csv_utils.get_row(hotend, "hotend_id", hotend_id))
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

    hotend = csv_utils.change_cell(hotend, "hotend_id", hotend_id, column, new_value)
    csv_utils.write_data([hotend_path], [hotend])


def update_hotend_maintenance(
    hotend: pd.DataFrame, maintenance: pd.DataFrame, maintenance_path: str | Path
) -> None:
    """Create a maintenance event for a hotend.

    Prompts for a hotend ID, maintenance type (cleaning), and date.
    Appends the event to the maintenance history CSV file.

    Args:
        hotend: DataFrame containing hotend data.
        maintenance: DataFrame containing maintenance history.
        maintenance_path: Path to the maintenance history CSV file.
    """
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
def read_buildplate(
    buildplate_path: str | Path, buildplate_maintenance_path: str | Path
) -> None:
    """Read buildplate data and maintenance history, then present a menu for updates.

    Reads the buildplate and buildplate maintenance CSV files, displays their
    contents, and prompts the user to edit a buildplate, create a maintenance
    event, or return to the home page.

    Args:
        buildplate_path: Path to the buildplate CSV file.
        buildplate_maintenance_path: Path to the buildplate maintenance history CSV file.
    """
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


def edit_buildplate(buildplate: pd.DataFrame, buildplate_path: str | Path) -> None:
    """Edit a buildplate's company or type.

    Displays all buildplates, prompts for a buildplate ID and the field to edit,
    then saves the change to the CSV file.

    Args:
        buildplate: DataFrame containing buildplate data.
        buildplate_path: Path to the buildplate CSV file.
    """
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
        buildplate, "buildplate_id", buildplate_id, column, new_value
    )
    csv_utils.write_data([buildplate_path], [buildplate])


def update_buildplate_maintenance(
    buildplate: pd.DataFrame, maintenance: pd.DataFrame, maintenance_path: str | Path
) -> None:
    """Create a maintenance event for a buildplate.

    Prompts for a buildplate ID, maintenance type (cleaning), and date.
    Appends the event to the maintenance history CSV file.

    Args:
        buildplate: DataFrame containing buildplate data.
        maintenance: DataFrame containing maintenance history.
        maintenance_path: Path to the maintenance history CSV file.
    """
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
def read_ams(ams_path: str | Path, ams_maintenance_path: str | Path) -> None:
    """Read AMS data and maintenance history, then present a menu for updates.

    Reads the AMS and AMS maintenance CSV files, displays their contents,
    and prompts the user to edit an AMS, create a maintenance event, or return
    to the home page.

    Args:
        ams_path: Path to the AMS CSV file.
        ams_maintenance_path: Path to the AMS maintenance history CSV file.
    """
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


def edit_ams(ams: pd.DataFrame, ams_path: str | Path) -> None:
    """Edit an AMS model.

    Displays all AMS units, prompts for an AMS ID and the new model value,
    then saves the change to the CSV file.

    Args:
        ams: DataFrame containing AMS data.
        ams_path: Path to the AMS CSV file.
    """
    # Get ams to edit
    print(ams.to_string(index=False))
    print("Enter ID of AMS to edit model")
    ams_id = int(input())

    # Get edited value
    print("What is the new AMS model")
    new_value = input()

    # Save
    ams = csv_utils.change_cell(ams, "ams_id", ams_id, "ams_model", new_value)


def update_ams_maintenance(
    ams: pd.DataFrame, maintenance: pd.DataFrame, maintenance_path: str | Path
) -> None:
    """Create a maintenance event for an AMS.

    Prompts for an AMS ID, maintenance type (desiccant change or firmware
    update), date, and optionally the firmware version. Appends the event
    to the maintenance history CSV file.

    Args:
        ams: DataFrame containing AMS data.
        maintenance: DataFrame containing maintenance history.
        maintenance_path: Path to the maintenance history CSV file.
    """
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
            firmware_version: str | None = None
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
def read_filament_dryers(dryer_path: str | Path, dryer_events_path: str | Path) -> None:
    """Read filament dryer data and usage history, then present a menu for updates.

    Reads the dryer and dryer events CSV files, displays their contents,
    and prompts the user to edit a dryer or return to the home page.

    Args:
        dryer_path: Path to the dryer CSV file.
        dryer_events_path: Path to the dryer events CSV file.
    """
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


def edit_dryer(dryers: pd.DataFrame, dryer_path: str | Path) -> None:
    """Edit a filament dryer's company, model, capacity, or temperature range.

    Displays all dryers, prompts for a dryer ID and the field to edit,
    then saves the change to the CSV file.

    Args:
        dryers: DataFrame containing dryer data.
        dryer_path: Path to the dryer CSV file.
    """
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
            column = "min_temp"
        case 5:
            column = "max_temp"

    # Save change
    dryers = csv_utils.change_cell(dryers, "dryer_id", dryer_id, column, new_value)
    csv_utils.write_data([dryer_path], [dryers])
