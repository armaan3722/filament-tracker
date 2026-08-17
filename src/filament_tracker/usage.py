from pathlib import Path

from filament_tracker import csv_utils


# FILAMENT USAGE
def add_filament_usage(
    projects_path: str | Path,
    categories_path: str | Path,
    collections_path: str | Path,
    print_jobs_path: str | Path,
    printer_path: str | Path,
    ams_path: str | Path,
    hotend_path: str | Path,
    buildplate_path: str | Path,
    filament_path: str | Path,
    filament_used_path: str | Path,
) -> None:
    """Record a new print job and filament usage.

    Prompts the user for project, collection, print job, and filament details,
    then updates the relevant CSV files. It also decrements filament stock and
    accumulates printer usage seconds.

    Args:
        projects_path: Path to the projects CSV file.
        categories_path: Path to the categories CSV file.
        collections_path: Path to the collections CSV file.
        print_jobs_path: Path to the print jobs CSV file.
        printer_path: Path to the printer CSV file.
        ams_path: Path to the AMS CSV file.
        hotend_path: Path to the hotend CSV file.
        buildplate_path: Path to the buildplate CSV file.
        filament_path: Path to the filament CSV file.
        filament_used_path: Path to the filament used CSV file.
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
            projects_path,
            categories_path,
            collections_path,
            print_jobs_path,
            printer_path,
            ams_path,
            hotend_path,
            buildplate_path,
            filament_path,
            filament_used_path,
        ]
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

        # Changing value types
        if has_config == "T":
            has_config = True
        else:
            has_config = False

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
            ],
            collections,
        )
        csv_utils.write_data([collections_path], [collections])

    # Get the rest of the print job and filament usage information

    # Print job information
    print("Enter the date printed")
    date = input()
    print("Enter the length of print")
    time = input()
    print("Enter the time taken to prepare print")
    prep_time = input()
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

    # Update filament left and printer hours used
    print_jobs = csv_utils.add_row(
        [
            len(print_jobs),
            date,
            time,
            prep_time,
            printer_id,
            ams_id,
            hotend_id,
            buildplate_id,
            collection_id,
            None,
            None,
            None,
            None,
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

    array_time = time.split()
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

    printer_seconds += print_job_seconds - print_job_prep_seconds
    printer_operation_seconds += print_job_seconds

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
        [print_jobs_path, filament_used_path, printer_path, filament_path],
        [print_jobs, filament_used, printer, filament],
    )

    # Add code for creation and selection of configs later


# NON PRINTED PARTS
def add_parts(
    projects_path: str | Path, categories_path: str | Path, collections_path: str | Path
) -> None:
    """Record a non-printed part by creating or selecting a collection.

    Prompts the user for project details and collection information,
    creating a new collection if needed, then saves it to the CSV file.

    Args:
        projects_path: Path to the projects CSV file.
        categories_path: Path to the categories CSV file.
        collections_path: Path to the collections CSV file.
    """
    # Get dataframes
    projects, categories, collections = csv_utils.read_data(
        [projects_path, categories_path, collections_path]
    )

    # Get project information
    print(projects.to_string(index=False))
    print("Enter project ID")
    project_id = input()

    if project_id != "":
        project_id = int(project_id)
    else:
        project_id = None

    # Get collection
    print("\n\nWould you like to select a collection(1) or create a new collection(2)")
    collection_action = int(input())

    match collection_action:
        case 1:
            print("\n\n" + collections.to_string(index=False))
            print("Enter collection ID")
            collection_id = int(input())
        case 2:
            print("\n\n")
            print("Enter collection name")
            collection_name = input()
            if collection_name == "":
                collection_name = None
            print("\n")

            print(categories.to_csv(index=False))
            print("Enter category ID")
            category_id = int(input())
            if category_id == "":
                category_id = None
            print("\n")

            print("Enter purpose of collection")
            purpose = input()
            if purpose == "":
                purpose = None
            print("Enter stage of collection")
            stage = input()
            if stage == "":
                stage = None
            print("\n")

            print("Enter version")
            version = int(input())
            if version == "":
                version = None
            print("Enter revision")
            revision = int(input())
            if revision == "":
                revision = None
            print("\n")

            print("Does this have a config (T/f)")
            has_config = input()
            if has_config == "T":
                has_config = True
                print("What quantity does it produce")
                quantity_produced = input()
            else:
                has_config = False
                quantity_produced = None

            collection_id = len(collections)
            collections = csv_utils.add_row(
                [
                    collection_id,
                    collection_name,
                    project_id,
                    purpose,
                    stage,
                    category_id,
                    version,
                    revision,
                    has_config,
                    quantity_produced,
                ],
                collections,
            )
            csv_utils.write_data([collections_path], [collections])
