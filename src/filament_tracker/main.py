# Import modules
import os
from importlib.resources import files
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from platformdirs import PlatformDirs

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

# todo: json metadata

# Create empty dictionary and platformdirs object
user_data_file_paths = {}
dirs = PlatformDirs("filament-tracker", appauthor=False)

# Get path based on environment variables
if dev_user_data_dir:
    data_dir = Path(dev_user_data_dir)
else:
    data_dir = dirs.user_data_path

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


# Main loop
def main():
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
