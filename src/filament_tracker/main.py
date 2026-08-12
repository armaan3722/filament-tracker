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

# List all file names
user_data_file_names = {
    "printers": "printers.csv",
    "printer_maintenance": "printer_maintenance.csv",
    "hotends": "hotends.csv",
    "hotend_maintenance": "hotend_maintenance.csv",
    "buildplates": "buildplates.csv",
    "buildplate_maintenance": "buildplate_maintenance.csv",
    "ams": "ams.csv",
    "ams_maintenance": "ams_maintenance.csv",
    "filament": "filament.csv",
    "filament_dryers": "filament_dryers.csv",
    "filament_dryer_events": "filament_dryer_events.csv",
    "spools": "spools.csv",
    "parts": "parts.csv",
    "purchases": "purchases.csv",
    "projects": "projects.csv",
    "categories": "categories.csv",
    "collections": "collections.csv",
    "print_jobs": "print_jobs.csv",
    "filament_used": "filament_used.csv",
    "plate_configs": "plate_configs.csv",
    "filament_configs": "filament_configs.csv",
}

# Create empty dictionary and platformdirs object
user_data_file_paths: dict[str, Path] = {}

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
def get_paths(data_dir: Path) -> None:
    """Gets the paths to all data files.

    Uses the given data_dir and the dictionary user_data_file_names to
    get the full path to each data file, and stores them into
    user_data_file_paths.  After, it checks each path, and if any file
    doesn't exist, it creates a new one based on the default_data files.

    Args:
        data_dir: The path to the data directory.
    """
    # Get full path including file name from dir
    for key, value in user_data_file_names.items():
        user_data_file_paths[key] = data_dir / value

    # Check if directory exists, and add default files if needed
    for value in user_data_file_paths.values():
        if not value.exists():
            # Get path of default files, and make dir for user data files
            default_path = files("filament_tracker") / "default_data" / value.name
            data_dir.mkdir(parents=True, exist_ok=True)

            # Read default file and write to user data dir
            pd.read_csv(str(default_path)).to_csv(data_dir / value.name, index=False)


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
    get_paths(data_dir)
    get_metadata(data_dir)

    run_loop = True
    while run_loop:
        # Start home screen
        print(
            "Would you like to view printer information(1), hotend information(2), build plate information(3), AMS information(4), \nfilament information(5), filament dryer information(6), reusable spools information(7), \nfilament storage information(8), non printed parts information(9), project information(10), \nprint history(11), purchases(12), update filament usage(13), or end program(14)"
        )
        action = int(input())

        # Run function
        match action:
            case 1:
                equipment.read_printer(
                    user_data_file_paths["printers"],
                    user_data_file_paths["printer_maintenance"],
                )
            case 2:
                equipment.read_hotend(
                    user_data_file_paths["hotends"],
                    user_data_file_paths["hotend_maintenance"],
                )
            case 3:
                equipment.read_buildplate(
                    user_data_file_paths["buildplates"],
                    user_data_file_paths["buildplate_maintenance"],
                )
            case 4:
                equipment.read_ams(
                    user_data_file_paths["ams"], user_data_file_paths["ams_maintenance"]
                )
            case 5:
                materials.read_filament(
                    user_data_file_paths["filament"],
                    user_data_file_paths["filament_dryers"],
                    user_data_file_paths["filament_dryer_events"],
                )
            case 6:
                equipment.read_filament_dryers(
                    user_data_file_paths["filament_dryers"],
                    user_data_file_paths["filament_dryer_events"],
                )
            case 7:
                materials.read_spools(user_data_file_paths["spools"])
            case 8:
                print(8)
            case 9:
                materials.read_parts(user_data_file_paths["parts"])
            case 10:
                projects.read_projects(
                    user_data_file_paths["projects"], user_data_file_paths["categories"]
                )
            case 11:
                print(11)
            case 12:
                purchase.view_purchases(
                    [
                        user_data_file_paths["printers"],
                        user_data_file_paths["hotends"],
                        user_data_file_paths["buildplates"],
                        user_data_file_paths["ams"],
                        user_data_file_paths["filament"],
                        user_data_file_paths["filament_dryers"],
                        user_data_file_paths["spools"],
                        user_data_file_paths["parts"],
                        user_data_file_paths["purchases"],
                    ]
                )
            case 13:
                usage.add_filament_usage(
                    user_data_file_paths["projects"],
                    user_data_file_paths["categories"],
                    user_data_file_paths["collections"],
                    user_data_file_paths["print_jobs"],
                    user_data_file_paths["printers"],
                    user_data_file_paths["ams"],
                    user_data_file_paths["hotends"],
                    user_data_file_paths["buildplates"],
                    user_data_file_paths["filament"],
                    user_data_file_paths["filament_used"],
                )
            case 14:
                print("Ending program")
                run_loop = False
