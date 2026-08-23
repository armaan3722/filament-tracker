# Import modules
import json
import os
from importlib.metadata import version
from importlib.resources import files
from pathlib import Path
from typing import Any

import pandas as pd
from dotenv import load_dotenv
from packaging.version import parse
from platformdirs import user_data_path

from filament_tracker import equipment, materials, projects, purchase, usage

# Load environment variables
load_dotenv()
dev_user_data_dir = os.getenv("DEV_USER_DATA_DIR")

# Constants for the newest program, data, and metadata versions
NEWEST_VERSION = version("filament_tracker")
NEWEST_DATA_VERSION = 1
NEWEST_METADATA_VERSION = 1


def get_data_dir() -> Path:
    """Gets the directory to store user data.

    Checks if the dev_user_data_dir variable has been set, and returns
    it's path if exists.  If not, it returns the directory given by
    platformdirs.

    Returns:
        The path that the user data should be stored in and
            accessed from
    """
    # Get path based on environment variables
    if dev_user_data_dir:
        data_dir = Path(dev_user_data_dir)
    else:
        data_dir = user_data_path("filament_tracker", appauthor=False)

    return data_dir


# Get paths of all data files
def get_paths(data_dir: Path) -> dict[str, dict[str, Any]]:
    """Builds full paths to all user data files and creates missing ones.

    Loads the schema definitions from datasets.json, appends the full
    file path to each entry, and creates any missing CSV files from
    the default_data templates.

    Args:
        data_dir: The path to the user data directory.

    Returns:
        A dictionary mapping entity names to their metadata,
        including filename, filepath, and schema.
    """
    # Read the datasets.json file
    with open(str(files("filament_tracker") / "datasets.json"), "r") as f:
        datasets = json.load(f)

    # Add full file paths to datasets
    for key, value in datasets.items():
        datasets[key]["filepath"] = data_dir / value["filename"]

    # Create default files if some files don't exist
    for value in datasets.values():
        if not value["filepath"].exists():
            default_path = (
                files("filament_tracker") / "default_data" / value["filepath"].name
            )
            data_dir.mkdir(parents=True, exist_ok=True)
            pd.read_csv(str(default_path)).to_csv(value["filepath"], index=False)

    return datasets


# Get metadata
def get_metadata(data_dir: Path) -> None:
    """Get the metadata JSON file.

    Gets full path to the metadata file based on data_dir parameter,
    assuming metadata file is called metadata.json.  If that path does
    not exist, it creates a new file at that path from the default_data
    file. Finally, runs check_for_migration function.

    Args:
        data_dir: The directory that the metadata file should be
            stored in.
    """
    # Get path to metadata file
    metadata_path = data_dir / "metadata.json"

    # Get default metadata
    if not metadata_path.exists():
        # Get the default path
        default_path = files("filament_tracker") / "default_data" / "metadata.json"
        data_dir.mkdir(parents=True, exist_ok=True)

        # Read the file from the default path, and write to the data path
        with open(str(default_path), "r") as f:
            metadata = json.load(f)

        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

    else:
        with open(metadata_path, "r") as f:
            metadata = json.load(f)

    # Check for required migration steps
    check_for_migration(metadata, metadata_path)


# Check if migration steps are required, and do the correct ones
def check_for_migration(metadata: dict[str, Any], metadata_path: Path) -> None:
    """Checks if migration functions are required, and runs the
    required ones.

    Compares the versions given by the metadata file to the newest
    versions.  If any do not match, it checks if migration steps are
    required, calls migration functions if applicable, and updates the
    metadata file with the new version.

    Args:
        metadata: The data from the metadata file.
        metadata_path: The path to the metadata file.
    """
    write_required = False

    if parse(metadata["version"]) != parse(NEWEST_VERSION):
        metadata["version"] = NEWEST_VERSION
        write_required = True

    if metadata["data_version"] != NEWEST_DATA_VERSION:
        metadata["data_version"] = NEWEST_DATA_VERSION
        write_required = True

    if metadata["metadata_version"] != NEWEST_METADATA_VERSION:
        metadata["metadata_version"] = NEWEST_METADATA_VERSION
        write_required = True

    if write_required:
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)


# Main loop
def main() -> None:
    """Run the main loop.

    Runs all functions that are required to make the application work.
    """
    data_dir = get_data_dir()
    datasets = get_paths(data_dir)
    get_metadata(data_dir)

    run_loop = True
    while run_loop:
        # Start home screen
        print(
            "Would you like to view printer information(1), hotend information(2), build plate information(3), \nAMS information(4), filament information(5), filament dryer information(6), reusable spools information(7), \nfilament storage information(8), non printed parts information(9), project information(10), \nprint history(11), parts usage history(12), purchases(13), update filament usage(14), \nupdate parts usage(15), or end program(16)"
        )
        action = int(input())

        # Run function
        match action:
            case 1:
                equipment.read_printer(
                    datasets["printers"],
                    datasets["printer_maintenance"],
                )
            case 2:
                equipment.read_hotend(
                    datasets["hotends"],
                    datasets["hotend_maintenance"],
                )
            case 3:
                equipment.read_buildplate(
                    datasets["buildplates"],
                    datasets["buildplate_maintenance"],
                )
            case 4:
                equipment.read_ams(datasets["ams"], datasets["ams_maintenance"])
            case 5:
                materials.read_filament(
                    datasets["filament"],
                    datasets["filament_dryers"],
                    datasets["filament_dryer_events"],
                )
            case 6:
                equipment.read_filament_dryers(
                    datasets["filament_dryers"],
                    datasets["filament_dryer_events"],
                )
            case 7:
                materials.read_spools(datasets["spools"])
            case 8:
                print(8)
            case 9:
                materials.read_parts(datasets["parts"])
            case 10:
                projects.read_projects(datasets["projects"], datasets["categories"])
            case 11:
                usage.view_print_history(
                    datasets["print_jobs"],
                    datasets["filament_used"],
                    datasets["filament"],
                )
            case 12:
                usage.view_parts_usage_history(datasets["parts_usage"])
            case 13:
                purchase.view_purchases(
                    [
                        datasets["printers"],
                        datasets["hotends"],
                        datasets["buildplates"],
                        datasets["ams"],
                        datasets["filament"],
                        datasets["filament_dryers"],
                        datasets["spools"],
                        datasets["parts"],
                        datasets["purchases"],
                    ]
                )
            case 14:
                usage.add_filament_usage(
                    datasets["projects"],
                    datasets["categories"],
                    datasets["collections"],
                    datasets["print_jobs"],
                    datasets["printers"],
                    datasets["ams"],
                    datasets["hotends"],
                    datasets["buildplates"],
                    datasets["filament"],
                    datasets["filament_used"],
                )
            case 15:
                usage.add_parts_usage(datasets["projects"], datasets["categories"], datasets["collections"], datasets["parts"], datasets["parts_usage"])
            case 16:
                print("Ending program")
                run_loop = False
