from typing import Any

import pandas as pd

from filament_tracker import csv_utils


def view_purchases(all_meta: list[dict[str, Any]]) -> None:
    """View purchase history and present a menu for updates.

    Reads the purchases CSV file, displays the purchase history,
    and prompts the user to add a purchase, edit a purchase, or return
    to the home page.

    Args:
        all_meta: List of all metadata dicts, with the last element being the
            purchases metadata dict.
    """
    # Read dataframe
    purchases = csv_utils.read_data([all_meta[-1]])[0]

    # Print purchase history
    print(purchases.to_string(index=False))

    # Update
    print(
        "Would you like to add a purchase(1), edit a purchase(2), or return to home(3)"
    )
    action = int(input())

    match action:
        case 1:
            add_purchases(all_meta)
        case 2:
            print(2)
        case 3:
            print("Returning to home")


def add_purchases(all_meta: list[dict[str, Any]]) -> None:
    """Record a new purchase of equipment and materials.

    Prompts for quantities of each item type being purchased (printers,
    hotends, buildplates, AMS, filament, dryers, spools, parts), then
    collects details for each item and updates the relevant CSV files.

    Args:
        all_meta: List of metadata dicts in order: printers, hotends,
            buildplates, AMS, filament, dryers, spools, parts, purchases.
    """
    # Read dataframes
    (
        printers,
        hotends,
        buildplates,
        ams,
        filament,
        dryers,
        spools,
        parts,
        purchases,
    ) = csv_utils.read_data(all_meta)

    if len(purchases) == 0:
        purchase_id = 0
    else:
        purchase_id = purchases.iloc[-1]["purchaseID"] + 1

    # Get purchases required
    print("How many printers were purchased")
    printers_purchased = int(input())
    print("How many hotends were purchased")
    hotends_purchased = int(input())
    print("How many buildplates were purchased")
    buildplates_purchased = int(input())
    print("How many AMS were purchased")
    ams_purchased = int(input())
    print("How many filament were purchased")
    filament_purchased = int(input())
    print("How many filament dryers were purchased")
    dryers_purchased = int(input())
    print("How many spools were purchased")
    spools_purchased = int(input())
    print("How many parts were purchased")
    parts_purchased = int(input())

    i = 0
    while i < printers_purchased:
        add_printer(printers, all_meta[0], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < hotends_purchased:
        add_hotend(hotends, all_meta[1], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < buildplates_purchased:
        add_buildplate(buildplates, all_meta[2], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < ams_purchased:
        add_ams(ams, all_meta[3], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < filament_purchased:
        add_filament(filament, all_meta[4], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < dryers_purchased:
        add_dryer(dryers, all_meta[5], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < spools_purchased:
        add_spool(spools, all_meta[6], purchases, all_meta[-1], purchase_id)
        i += 1

    i = 0
    while i < parts_purchased:
        add_parts(parts, all_meta[7], purchases, all_meta[-1], purchase_id)
        i += 1


def add_printer(
    printer: pd.DataFrame,
    printer_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased printer and record the purchase.

    Prompts for printer details (company, model, name, seller, cost, dates),
    appends rows to both the printer and purchases DataFrames, then saves
    them to their respective CSV files.

    Args:
        printer: DataFrame containing printer data.
        printer_meta: Dict containing printer metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get new printer information
    print("What is the new printer company")
    new_printer_company = input()
    print("What is the new printer model")
    new_printer_model = input()
    print("What is the new printer name")
    new_printer_name = input()
    print("Where was it purchased from")
    seller = input()
    print("What is the new printer cost")
    new_printer_cost = input()
    print("What is the new printer date purchased")
    new_printer_date = input()
    print("What is the new printer date arrived")
    new_printer_arrival_date = input()

    # Update dataframes
    printer = csv_utils.add_row(
        [len(printer), new_printer_name, new_printer_company, new_printer_model, 0, 0],
        printer,
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Printer",
            seller,
            len(printer) - 1,
            new_printer_date,
            new_printer_arrival_date,
            new_printer_cost,
        ],
        purchases,
    )

    # Save
    csv_utils.write_data([printer_meta, purchases_meta], [printer, purchases])


def add_hotend(
    hotend: pd.DataFrame,
    hotend_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased hotend and record the purchase.

    Prompts for hotend details (company, size, material, seller, cost, dates),
    appends rows to both the hotend and purchases DataFrames, then saves
    them to their respective CSV files.

    Args:
        hotend: DataFrame containing hotend data.
        hotend_meta: Dict containing hotend metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get hotend to add
    print("What is the new hotend company")
    new_hotend_company = input()
    print("What is the new hotend size")
    new_hotend_size = input()
    print("What is the new hotend material")
    new_hotend_material = input()
    print("Where was it purchased from")
    seller = input()
    print("What is the date purchased")
    new_hotend_date = input()
    print("What is the date arrived")
    new_hotend_arrival_date = input()
    print("What is the new hotend cost")
    new_hotend_cost = input()

    # Update dataframes
    hotend = csv_utils.add_row(
        [
            len(hotend),
            new_hotend_company,
            new_hotend_size,
            new_hotend_material,
            "Passive",
        ],
        hotend,
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Hotend",
            seller,
            len(hotend) - 1,
            new_hotend_date,
            new_hotend_arrival_date,
            new_hotend_cost,
        ],
        purchases,
    )
    csv_utils.write_data([hotend_meta, purchases_meta], [hotend, purchases])


def add_buildplate(
    buildplate: pd.DataFrame,
    buildplate_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased buildplate and record the purchase.

    Prompts for buildplate details (company, type, seller, dates, cost),
    appends rows to both the buildplate and purchases DataFrames, then saves
    them to their respective CSV files.

    Args:
        buildplate: DataFrame containing buildplate data.
        buildplate_meta: Dict containing buildplate metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get buildplate to add
    print("What company is the buildplate from")
    buildplate_company = input()
    print("What type of build plate is it")
    buildplate_type = input()
    print("Where was it purchased from")
    seller = input()
    print("What is the date purchased")
    purchase_date = input()
    print("What is the date arrived")
    arrival_date = input()
    print("What is the cost")
    cost = input()

    # Add to csv files
    buildplate = csv_utils.add_row(
        [len(buildplate), buildplate_company, buildplate_type], buildplate
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Buildplate",
            seller,
            len(buildplate) - 1,
            purchase_date,
            arrival_date,
            cost,
        ],
        purchases,
    )
    csv_utils.write_data([buildplate_meta, purchases_meta], [buildplate, purchases])


def add_ams(
    ams: pd.DataFrame,
    ams_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased AMS and record the purchase.

    Prompts for AMS details (model, seller, dates, cost), appends rows
    to both the AMS and purchases DataFrames, then saves them to their
    respective CSV files.

    Args:
        ams: DataFrame containing AMS data.
        ams_meta: Dict containing AMS metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get AMS to add
    print("What AMS model is added")
    ams_model = input()
    print("Where was it purchased from")
    seller = input()
    print("What date was this purchased")
    purchase_date = input()
    print("What date did the ams arrive")
    arrival_date = input()
    print("What did the AMS cost")
    cost = input()

    # Update dataframes
    ams = csv_utils.add_row([len(ams), ams_model], ams)
    purchases = csv_utils.add_row(
        [purchase_id, "AMS", seller, len(ams) - 1, purchase_date, arrival_date, cost],
        purchases,
    )
    csv_utils.write_data([ams_meta, purchases_meta], [ams, purchases])


def add_filament(
    filament: pd.DataFrame,
    filament_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add newly purchased filament and record the purchase.

    Prompts for filament details (company, colour, material, diameter,
    starting amount, seller, dates, cost), appends rows to both the
    filament and purchases DataFrames, then saves them to their
    respective CSV files.

    Args:
        filament: DataFrame containing filament data.
        filament_meta: Dict containing filament metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get information
    print("What is the new filament company")
    company = input()
    print("What is the new filament colour")
    colour = input()
    print("What is the new filament material")
    material = input()
    print("What is the new filament diameter")
    diameter = input()
    print("What is the new filament starting amount")
    starting_amount = input()
    print("Where was it purchased from")
    seller = input()
    print("What is the date purchased")
    date_purchased = input()
    print("What is the date arrived")
    arrival_date = input()
    print("What is the cost")
    cost = input()

    # Update dataframes
    filament = csv_utils.add_row(
        [
            len(filament),
            company,
            colour,
            material,
            diameter,
            starting_amount,
            starting_amount,
            "Waiting",
            None,
        ],
        filament,
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Filament",
            seller,
            len(filament) - 1,
            date_purchased,
            arrival_date,
            cost,
        ],
        purchases,
    )
    csv_utils.write_data([filament_meta, purchases_meta], [filament, purchases])


def add_dryer(
    dryers: pd.DataFrame,
    dryers_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased filament dryer and record the purchase.

    Prompts for dryer details (company, model, capacity, temperature
    range, seller, dates, cost), appends rows to both the dryers and
    purchases DataFrames, then saves them to their respective CSV files.

    Args:
        dryers: DataFrame containing dryer data.
        dryers_meta: Dict containing dryer metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get information about dryer
    print("What is the company for the filament dryer")
    company = input()
    print("What is the model of filament dryer")
    model = input()
    print("What is the capacity of the dryer")
    capacity = input()
    print("What is the min temperature")
    min_temp = input()
    print("What is the max temp")
    max_temp = input()
    print("Where was it purchased from")
    seller = input()
    print("What is the date of purchase")
    purchase_date = input()
    print("What is the date of arrival")
    arrival_date = input()
    print("What is the cost")
    cost = input()

    # Update information
    dryers = csv_utils.add_row(
        [len(dryers), company, model, capacity, min_temp, max_temp], dryers
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Filament Dryer",
            seller,
            len(dryers) - 1,
            purchase_date,
            arrival_date,
            cost,
        ],
        purchases,
    )
    csv_utils.write_data([dryers_meta, purchases_meta], [dryers, purchases])


def add_spool(
    spools: pd.DataFrame,
    spool_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add a newly purchased reusable spool and record the purchase.

    Prompts for spool type and purchase details (dates, cost), appends
    rows to both the spools and purchases DataFrames, then saves them
    to their respective CSV files.

    Args:
        spools: DataFrame containing spool data.
        spool_meta: Dict containing spool metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get information about purchase
    print("What is the type of spool")
    spool_type = input()
    print("What is the date purchased")
    date_purchased = input()
    print("What is the date arrived")
    date_arrived = input()
    print("What is the cost")
    cost = input()

    # Update information
    spools = csv_utils.add_row([len(spools), spool_type], spools)
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Reusable spool",
            "Bambu",
            len(spools) - 1,
            date_purchased,
            date_arrived,
            cost,
        ],
        purchases,
    )
    csv_utils.write_data([spool_meta, purchases_meta], [spools, purchases])


def add_parts(
    parts: pd.DataFrame,
    parts_meta: dict[str, Any],
    purchases: pd.DataFrame,
    purchases_meta: dict[str, Any],
    purchase_id: int,
) -> None:
    """Add newly purchased parts and record the purchase.

    Prompts for part details (type, spec, amount, dates, cost, seller),
    appends rows to both the parts and purchases DataFrames, then saves
    them to their respective CSV files.

    Args:
        parts: DataFrame containing parts data.
        parts_meta: Dict containing parts metadata with 'filepath' key.
        purchases: DataFrame containing purchase history.
        purchases_meta: Dict containing purchases metadata with 'filepath' key.
        purchase_id: ID for the current purchase record.
    """
    # Get information about purchase
    print("What is the part type")
    part_type = input()
    print("What is the part spec")
    part_spec = input()
    print("What amount was purchased")
    amount_purchased = input()
    print("What was the date purchased")
    date_purchased = input()
    print("What was the date arrived")
    date_arrived = input()
    print("What is the cost")
    cost = input()
    print("Where was it purchased")
    seller = input()

    # Add information to csv
    parts = csv_utils.add_row(
        [len(parts), part_type, part_spec, amount_purchased, amount_purchased], parts
    )
    purchases = csv_utils.add_row(
        [
            purchase_id,
            "Parts",
            seller,
            len(parts) - 1,
            date_purchased,
            date_arrived,
            cost,
        ],
        purchases,
    )
    csv_utils.write_data([parts_meta, purchases_meta], [parts, purchases])
