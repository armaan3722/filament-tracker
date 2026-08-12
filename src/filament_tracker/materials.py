from pathlib import Path

import pandas as pd

from filament_tracker import csv_utils


# FILAMENT
def read_filament(
    filament_path: str | Path, dryer_path: str | Path, dryer_events_path: str | Path
) -> None:
    """Read filament data and drying events, then present a menu for updates.

    Reads the filament, dryer, and dryer events CSV files, displays filament
    data, and prompts the user to edit a filament, add a drying event, or
    return to the home page.

    Args:
        filament_path: Path to the filament CSV file.
        dryer_path: Path to the dryer CSV file.
        dryer_events_path: Path to the dryer events CSV file.
    """
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


def edit_filament(filament: pd.DataFrame, filament_path: str | Path) -> None:
    """Edit a filament's company, colour, material, diameter, starting amount, or state.

    Displays all filaments, prompts for a filament ID and the field to edit,
    then saves the change to the CSV file.

    Args:
        filament: DataFrame containing filament data.
        filament_path: Path to the filament CSV file.
    """
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


def add_drying_event(
    filament: pd.DataFrame,
    filament_path: str | Path,
    dryers: pd.DataFrame,
    dryer_events: pd.DataFrame,
    dryer_events_path: str | Path,
) -> None:
    """Record a drying event for a filament roll.

    Prompts for a filament ID, dryer ID, drying duration, temperature, and date.
    Updates the filament's last dried date and appends the event to the
    dryer events CSV file.

    Args:
        filament: DataFrame containing filament data.
        filament_path: Path to the filament CSV file.
        dryers: DataFrame containing dryer data.
        dryer_events: DataFrame containing dryer events.
        dryer_events_path: Path to the dryer events CSV file.
    """
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
def read_spools(spool_path: str | Path) -> None:
    """Read reusable spool data, then present a menu for updates.

    Reads the spools CSV file, displays spool data, and prompts the user
    to edit a spool or return to the home page.

    Args:
        spool_path: Path to the spools CSV file.
    """
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


def edit_spool(spools: pd.DataFrame, spool_path: str | Path) -> None:
    """Edit a spool's type.

    Prompts for a spool ID and new type value, then saves the change
    to the CSV file.

    Args:
        spools: DataFrame containing spool data.
        spool_path: Path to the spools CSV file.
    """
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
def read_parts(parts_path: str | Path) -> None:
    """Read parts data, then present a menu for updates.

    Reads the parts CSV file, displays parts data, and prompts the user
    to edit a part or return to the home page.

    Args:
        parts_path: Path to the parts CSV file.
    """
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


def edit_parts(parts: pd.DataFrame, parts_path: str | Path) -> None:
    """Edit a part's type, spec, or starting quantity.

    Displays all parts, prompts for a part ID and the field to edit,
    then saves the change to the CSV file.

    Args:
        parts: DataFrame containing part data.
        parts_path: Path to the parts CSV file.
    """
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
