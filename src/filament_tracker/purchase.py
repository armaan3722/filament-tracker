from pathlib import Path

import pandas as pd

from filament_tracker import csv_utils


def view_purchases(all_paths: list[str | Path]) -> None:
    # Read dataframe
    purchases = csv_utils.read_data([all_paths[-1]])[0]

    # Print purchase history
    print(purchases.to_string(index=False))

    # Update
    print(
        "Would you like to add a purchase(1), edit a purchase(2), or return to home(3)"
    )
    action = int(input())

    match action:
        case 1:
            add_purchases(all_paths)
        case 2:
            print(2)
        case 3:
            print("Returning to home")


def add_purchases(all_paths: list[str | Path]) -> None:
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
    ) = csv_utils.read_data(all_paths)

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
        add_printer(printers, all_paths[0], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < hotends_purchased:
        add_hotend(hotends, all_paths[1], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < buildplates_purchased:
        add_buildplate(buildplates, all_paths[2], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < ams_purchased:
        add_ams(ams, all_paths[3], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < filament_purchased:
        add_filament(filament, all_paths[4], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < dryers_purchased:
        add_dryer(dryers, all_paths[5], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < spools_purchased:
        add_spool(spools, all_paths[6], purchases, all_paths[-1], purchase_id)
        i += 1

    i = 0
    while i < parts_purchased:
        add_parts(parts, all_paths[7], purchases, all_paths[-1], purchase_id)
        i += 1


def add_printer(
    printer: pd.DataFrame,
    path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([path, purchases_path], [printer, purchases])


def add_hotend(
    hotend: pd.DataFrame,
    hotend_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([hotend_path, purchases_path], [hotend, purchases])


def add_buildplate(
    buildplate: pd.DataFrame,
    buildplate_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([buildplate_path, purchases_path], [buildplate, purchases])


def add_ams(
    ams: pd.DataFrame,
    ams_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([ams_path, purchases_path], [ams, purchases])


def add_filament(
    filament: pd.DataFrame,
    filament_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([filament_path, purchases_path], [filament, purchases])


def add_dryer(
    dryers: pd.DataFrame,
    dryer_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([dryer_path, purchases_path], [dryers, purchases])


def add_spool(
    spools: pd.DataFrame,
    spool_path: str | Path,
    purchases: pd.DataFrame,
    purchase_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([spool_path, purchase_path], [spools, purchases])


def add_parts(
    parts: pd.DataFrame,
    parts_path: str | Path,
    purchases: pd.DataFrame,
    purchases_path: str | Path,
    purchase_id: int,
) -> None:
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
    csv_utils.write_data([parts_path, purchases_path], [parts, purchases])
