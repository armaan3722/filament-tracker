from datetime import UTC, datetime
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd
from tzlocal import get_localzone

from filament_tracker import csv_utils


# PRINT HISTORY
def view_print_history(
    print_jobs_meta: dict[str, Any],
    filament_used_meta: dict[str, Any],
    filament_meta: dict[str, Any],
) -> None:
    """View print history and optionally see filament usage for a specific job.

    Reads print job, filament used, and filament data from CSV files,
    displays the print history, and allows the user to view filament
    details for a selected print job.

    Args:
        print_jobs_meta: Dict containing print jobs metadata with 'filepath' key.
        filament_used_meta: Dict containing filament used metadata with 'filepath' key.
        filament_meta: Dict containing filament metadata with 'filepath' key.
    """
    # Get dataframes
    print_jobs, filament_used, filament = csv_utils.read_data(
        [print_jobs_meta, filament_used_meta, filament_meta]
    )
    print_jobs["print_date_and_time"] = (
        pd.to_datetime(print_jobs["print_date_and_time"], format="%Y-%m-%d %H:%M")
        .dt.tz_localize(UTC)
        .dt.floor("min")
        .dt.tz_convert(get_localzone())
    )

    # Print history info
    print("Print history:\n")
    print(print_jobs.to_string(index=False))

    # Get next action
    print(
        "\n\nWould you like to view filament used for a print job (1), or return to home (2)"
    )
    action = int(input())

    match action:
        case 1:
            # Get print job id
            print("Enter the ID of the print job to view filament for:")
            print_id = int(input())

            # Get filament for that job
            filament_used_per_job = csv_utils.get_row(
                filament_used, "print_id", print_id
            )
            print("\n\nFilament used:")
            print(filament_used_per_job.to_string(index=False))

            # Get the actual filament data for those id's
            unique_filament_ids = filament_used_per_job["filament_id"].unique()
            print("\n\nFilament:")
            print(
                filament[filament["filament_id"].isin(unique_filament_ids)].to_string(
                    index=False
                )
            )
        case 2:
            print("Returning to home page")


def view_parts_usage_history(
    parts_usage_meta: dict[str, Any],
) -> None:
    """View parts usage history.

    Read parts usage data from a CSV file, converts the datetime column
    to the local timezone, and displays the full history of parts usage.

    Args:
        parts_usage_meta: Dict containing parts usage metadata with 'filepath' key.
    """
    # Get dataframes
    parts_usage = csv_utils.read_data([parts_usage_meta])[0]

    parts_usage["usage_date_and_time"] = (
        pd.to_datetime(parts_usage["usage_date_and_time"], format="%Y-%m-%d %H:%M")
        .dt.tz_localize(UTC)
        .dt.floor("min")
        .dt.tz_convert(get_localzone())
    )

    # Print history info
    print("Parts usage history:\n")
    print(parts_usage.to_string(index=False))


# FILAMENT USAGE
def add_filament_usage(
    projects_meta: dict[str, Any],
    categories_meta: dict[str, Any],
    collections_meta: dict[str, Any],
    print_jobs_meta: dict[str, Any],
    printer_meta: dict[str, Any],
    ams_meta: dict[str, Any],
    hotend_meta: dict[str, Any],
    buildplate_meta: dict[str, Any],
    filament_meta: dict[str, Any],
    filament_used_meta: dict[str, Any],
) -> None:
    """Record a new print job and filament usage.

    Prompts the user for project, collection, print job, and filament details,
    then updates the relevant CSV files. It also decrements filament stock and
    accumulates printer usage seconds.

    Args:
        projects_meta: Dict containing projects metadata with 'filepath' key.
        categories_meta: Dict containing categories metadata with 'filepath' key.
        collections_meta: Dict containing collections metadata with 'filepath' key.
        print_jobs_meta: Dict containing print jobs metadata with 'filepath' key.
        printer_meta: Dict containing printer metadata with 'filepath' key.
        ams_meta: Dict containing AMS metadata with 'filepath' key.
        hotend_meta: Dict containing hotend metadata with 'filepath' key.
        buildplate_meta: Dict containing buildplate metadata with 'filepath' key.
        filament_meta: Dict containing filament metadata with 'filepath' key.
        filament_used_meta: Dict containing filament used metadata with 'filepath' key.
    """
    # Get dataframes
    (
        projects,
        categories,
        collections,
        print_jobs,
        printer,
        ams,
        hotend,
        buildplate,
        filament,
        filament_used,
    ) = csv_utils.read_data(
        [
            projects_meta,
            categories_meta,
            collections_meta,
            print_jobs_meta,
            printer_meta,
            ams_meta,
            hotend_meta,
            buildplate_meta,
            filament_meta,
            filament_used_meta,
        ]
    )

    # Convert print_jobs datetime column to datetime
    print_jobs["print_date_and_time"] = (
        pd.to_datetime(print_jobs["print_date_and_time"], format="%Y-%m-%d %H:%M")
        .dt.tz_localize(UTC)
        .dt.floor("min")
    )

    # Get project information
    print(projects)
    print("Enter project ID of print")
    project_id = int(input())

    # Get collection information, either pick a collection or create a new one
    print("Do you want to select a collection(1), or create a new collection(2)")
    collection_action = int(input())

    if collection_action == 1:
        print(print_jobs.to_string(index=False))
        print("\n\n")
        print(collections.to_string(index=False))
        print("\n\nEnter collection ID")
        collection_id = int(input())
        print_index = len(csv_utils.get_row(print_jobs, "collection_id", collection_id))
    else:
        print_index = 0
        print("\n\nWhat is the new collection name")
        collection_name = input()
        print(categories.to_string(index=False))
        print("Enter category ID")
        category_id = int(input())
        print("Enter purpose (press enter for same as category)")
        purpose = input()
        print("Enter stage (press enter for same as category)")
        stage = input()
        print("Enter version")
        version = input()
        print("Does this collection have configs (T/f)")
        has_config = input()
        print("What quantity does this collection produce")
        quantity_produced = input()
        print("Is this collection a clone (Y/n)")
        is_clone = input()

        # Set collection name to None if not given
        if collection_name == "":
            collection_name = None

        # Changing value types
        if has_config == "T":
            has_config = True
        else:
            has_config = False

        # Get clone information
        if is_clone == "Y":
            is_clone = True
            print(collections.to_string(index=False))
            print("\nEnter the collection cloned from")
            cloned_from = int(input())
        else:
            is_clone = False
            cloned_from = None

        # Handle null values
        test_array = [
            purpose,
            stage,
            version,
            has_config,
            quantity_produced,
        ]

        i = 0
        while i < len(test_array):
            if test_array[i] == "":
                test_array[i] = None
            i += 1

        # Save data
        collection_id = len(collections)
        collections = csv_utils.add_row(
            [
                collection_id,
                collection_name,
                project_id,
                category_id,
                test_array[0],
                test_array[1],
                test_array[2],
                test_array[3],
                test_array[4],
                is_clone,
                cloned_from,
            ],
            collections,
        )
        csv_utils.write_data([collections_meta], [collections])

    # Get the rest of the print job and filament usage information

    # Print job information
    print("Enter the name of the print")
    print_name = input()
    print("Enter the date and time printed (YYYY-MM-DD HH:MM, use 24 hour time)")
    date_and_time = input()
    print("Enter the timezone, press enter for current system timezone")
    user_timezone = input()
    print("Enter the length of just the print (d h m s)")
    length = input()
    print("Enter the time taken to prepare print (d h m s)")
    prep_time = input()
    print("Enter the amount of filament changes")
    filament_changes = int(input())
    print(printer.to_string(index=False))
    print("Enter printer ID")
    printer_id = int(input())
    print(ams.to_string(index=False))
    print("Enter ams ID if applicable")
    ams_id = int(input())
    print(hotend.to_string(index=False))
    print("Enter hotend ID")
    hotend_id = int(input())
    print(buildplate.to_string(index=False))
    print("Enter buildplate ID")
    buildplate_id = int(input())

    # Make print name None if not given
    if print_name == "":
        print_name = None

    # Get default timezone
    if user_timezone == "":
        user_timezone = get_localzone()
    else:
        user_timezone = ZoneInfo(user_timezone)

    # Convert frm string to datetime
    date_and_time = (
        datetime.strptime(date_and_time, "%Y-%m-%d %H:%M")
        .replace(tzinfo=user_timezone)
        .astimezone(UTC)
    )

    # Get filament used
    print("How many different spools of filament were used")
    spools_used = int(input())

    i = 0
    while i < spools_used:
        # Get information
        print(filament.to_string(index=False))
        print("Enter ID of filament used")
        filament_id = int(input())
        print("Enter amount of filament used in grams")
        filament_amount_printed = float(input())

        # Update information
        filament_used = csv_utils.add_row(
            [filament_id, filament_amount_printed, len(print_jobs)], filament_used
        )

        previous_filament_left = csv_utils.get_cell(
            filament, "filament_id", filament_id, "amount_left"
        )
        previous_filament_left -= filament_amount_printed

        filament = csv_utils.change_cell(
            filament, "filament_id", filament_id, "amount_left", previous_filament_left
        )

        i += 1

    # Get print success data
    print("Was the print successful (Y/n)")
    print_successful = input()

    if print_successful == "Y":
        print_successful = True
        failure_reason = None
        filament_lost = None
    else:
        print_successful = False
        print("What was the reason for failure")
        failure_reason = input()
        print("How much filament was lost to the failure")
        filament_lost = float(input())

    # Get repair print data
    print("Was this print a repair print (Y/n)")
    repair_print = input()

    if repair_print == "Y":
        repair_print = True

        print(print_jobs.to_string(index=False))
        print("\n\nHow many print jobs was this a repair print for")
        repair_print_amount = int(input())

        for i in range(repair_print_amount):
            print("What is the ID of the print job")
            repair_id = int(input())
            csv_utils.change_cell(
                print_jobs, "print_id", repair_id, "repair_print_id", repair_id
            )
    else:
        repair_print = False

    # Update filament left and printer hours used
    print_jobs = csv_utils.add_row(
        [
            len(print_jobs),
            print_index,
            print_name,
            date_and_time,
            user_timezone,
            length,
            prep_time,
            filament_changes,
            printer_id,
            ams_id,
            hotend_id,
            buildplate_id,
            collection_id,
            None,
            print_successful,
            failure_reason,
            filament_lost,
            repair_print,
            None,
        ],
        print_jobs,
    )

    printer_seconds = csv_utils.get_cell(
        printer, "printer_id", printer_id, "printer_seconds_used"
    )
    printer_operation_seconds = csv_utils.get_cell(
        printer, "printer_id", printer_id, "printer_seconds_in_operation"
    )

    array_time = length.split()
    array_prep_time = prep_time.split()

    print_job_seconds = (
        int(array_time[0]) * 86400
        + int(array_time[1]) * 3600
        + int(array_time[2]) * 60
        + int(array_time[3])
    )

    print_job_prep_seconds = (
        int(array_prep_time[0]) * 86400
        + int(array_prep_time[1]) * 3600
        + int(array_prep_time[2]) * 60
        + int(array_prep_time[3])
    )

    printer_seconds += print_job_seconds
    printer_operation_seconds += print_job_seconds + print_job_prep_seconds

    printer = csv_utils.change_cell(
        printer, "printer_id", printer_id, "printer_seconds_used", printer_seconds
    )
    printer = csv_utils.change_cell(
        printer,
        "printer_id",
        printer_id,
        "printer_seconds_in_operation",
        printer_operation_seconds,
    )

    csv_utils.write_data(
        [filament_used_meta, printer_meta, filament_meta],
        [filament_used, printer, filament],
    )

    print_jobs.to_csv(
        print_jobs_meta["filepath"], index=False, date_format="%Y-%m-%d %H:%M"
    )

    # Add code for creation and selection of configs later


# NON PRINTED PARTS
def add_parts_usage(
    projects_meta: dict[str, Any],
    categories_meta: dict[str, Any],
    collections_meta: dict[str, Any],
    parts_meta: dict[str, Any],
    parts_usage_meta: dict[str, Any],
) -> None:
    """Record a non-printed part by creating or selecting a collection.

    Prompts the user for project details and collection information,
    creating a new collection if needed, then records the part usage
    and updates the relevant CSV files. It also decrements the part
    stock in the parts table.

    Args:
        projects_meta: Dict containing projects metadata with 'filepath' key.
        categories_meta: Dict containing categories metadata with 'filepath' key.
        collections_meta: Dict containing collections metadata with 'filepath' key.
        parts_meta: Dict containing parts metadata with 'filepath' key.
        parts_usage_meta: Dict containing parts usage metadata with 'filepath' key.
    """
    # Get dataframes
    projects, categories, collections, parts, parts_usage = csv_utils.read_data(
        [projects_meta, categories_meta, collections_meta, parts_meta, parts_usage_meta]
    )

    # Convert parts_usage datetime column to datetime
    parts_usage["usage_date_and_time"] = (
        pd.to_datetime(parts_usage["usage_date_and_time"], format="%Y-%m-%d %H:%M")
        .dt.tz_localize(UTC)
        .dt.floor("min")
    )

    # Get project information
    print(projects.to_string(index=False))
    print("Enter project ID")
    project_id = int(input())

    # Get collection information, either pick a collection or create a new one
    print("Do you want to select a collection(1), or create a new collection(2)")
    collection_action = int(input())

    if collection_action == 1:
        print(parts_usage.to_string(index=False))
        print("\n\n")
        print(collections.to_string(index=False))
        print("\n\nEnter collection ID")
        collection_id = int(input())
    else:
        print("\n\nWhat is the new collection name")
        collection_name = input()
        print(categories.to_string(index=False))
        print("Enter category ID")
        category_id = int(input())
        print("Enter purpose (press enter for same as category)")
        purpose = input()
        print("Enter stage (press enter for same as category)")
        stage = input()
        print("Enter version")
        version = input()
        print("Does this collection have configs (T/f)")
        has_config = input()
        print("What quantity does this collection produce")
        quantity_produced = input()
        print("Is this collection a clone (Y/n)")
        is_clone = input()

        # Set collection name to None if not given
        if collection_name == "":
            collection_name = None

        # Changing value types
        if has_config == "T":
            has_config = True
        else:
            has_config = False

        # Get clone information
        if is_clone == "Y":
            is_clone = True
            print(collections.to_string(index=False))
            print("\nEnter the collection cloned from")
            cloned_from = int(input())
        else:
            is_clone = False
            cloned_from = None

        # Handle null values
        test_array = [
            purpose,
            stage,
            version,
            has_config,
            quantity_produced,
            is_clone,
            cloned_from,
        ]

        i = 0
        while i < len(test_array):
            if test_array[i] == "":
                test_array[i] = None
            i += 1

        # Save data
        collection_id = len(collections)
        collections = csv_utils.add_row(
            [
                collection_id,
                collection_name,
                project_id,
                category_id,
                test_array[0],
                test_array[1],
                test_array[2],
                test_array[3],
                test_array[4],
                is_clone,
                cloned_from,
            ],
            collections,
        )
        csv_utils.write_data([collections_meta], [collections])

    # Get the rest of the information

    print(parts.to_string(index=False))
    print("Enter the part id for part used")
    part_used_id = int(input())
    print("How many were used")
    amount_used = int(input())
    print("Enter the date and time used (YYYY-MM-DD HH:MM, use 24 hour time)")
    date_and_time = input()
    print("Enter the timezone, press enter for current system timezone")
    user_timezone = input()

    # Get default timezone
    if user_timezone == "":
        user_timezone = get_localzone()
    else:
        user_timezone = ZoneInfo(user_timezone)

    # Convert frm string to datetime
    date_and_time = (
        datetime.strptime(date_and_time, "%Y-%m-%d %H:%M")
        .replace(tzinfo=user_timezone)
        .astimezone(UTC)
    )

    remaining = (
        int(csv_utils.get_cell(parts, "part_id", part_used_id, "current_amount"))
        - amount_used
    )
    parts = csv_utils.change_cell(
        parts, "part_id", part_used_id, "current_amount", remaining
    )
    parts_usage = csv_utils.add_row(
        [
            len(parts_usage),
            date_and_time,
            user_timezone,
            part_used_id,
            amount_used,
            collection_id,
        ],
        parts_usage,
    )
    csv_utils.write_data([parts_meta], [parts])

    parts_usage.to_csv(
        parts_usage_meta["filepath"], index=False, date_format="%Y-%m-%d %H:%M"
    )
