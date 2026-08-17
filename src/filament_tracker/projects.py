from pathlib import Path

import pandas as pd

from filament_tracker import csv_utils


# PROJECTS
def read_projects(projects_path: str | Path, categories_path: str | Path) -> None:
    """Read projects and categories, then present a menu for updates.

    Reads the projects and categories CSV files, displays projects,
    and prompts the user to add/edit a project, view categories, or return
    to the home page.

    Args:
        projects_path: Path to the projects CSV file.
        categories_path: Path to the categories CSV file.
    """
    # Get dataframe
    projects, categories = csv_utils.read_data([projects_path, categories_path])

    # Print dataframe
    print("Projects:")
    print(projects.to_string(index=False))

    # Get action
    print(
        "\n\nWould you like to add a project(1), edit a project(2), view categories for a project(3), or return to home page(4)"
    )
    action = int(input())

    match action:
        case 1:
            add_project(projects, projects_path)
        case 2:
            edit_project(projects, projects_path)
        case 3:
            print("Enter ID of project to view categories for")
            project_id = int(input())
            read_categories(categories, categories_path, project_id)
        case 4:
            print("Returning to home page")


def add_project(projects: pd.DataFrame, projects_path: str | Path) -> None:
    """Add a new project to the projects CSV file.

    Prompts for a project name and appends a new row to the projects DataFrame.

    Args:
        projects: DataFrame containing project data.
        projects_path: Path to the projects CSV file.
    """
    # Get information about new project
    print("What is the new project name")
    name = input()

    # Update information
    projects = csv_utils.add_row([len(projects), name, "In progress"], projects)
    csv_utils.write_data([projects_path], [projects])


def edit_project(projects: pd.DataFrame, projects_path: str | Path) -> None:
    """Edit a project's name.

    Displays all projects, prompts for a project ID and new name,
    then saves the change to the CSV file.

    Args:
        projects: DataFrame containing project data.
        projects_path: Path to the projects CSV file.
    """
    # Get project to edit
    print(projects.to_string(index=False))
    print("Enter ID of project to edit")
    project_id = int(input())

    # Get value to edit
    print("Would you like to edit the project name (1), or project state (2)?")
    edit_type = int(input())
    print("Enter new value")
    new_value = input()

    # Get column to edit
    match edit_type:
        case 1:
            column = "project_name"
        case 2:
            column = "project_state"

    # Save data
    projects = csv_utils.change_cell(
        projects, "project_id", project_id, column, new_value
    )
    csv_utils.write_data([projects_path], [projects])


# CATEGORIES
def read_categories(
    categories: pd.DataFrame, categories_path: str | Path, project_id: int
) -> None:
    """Read categories for a project and present a menu for updates.

    Displays categories filtered by project ID and prompts the user to
    add/edit a category or return to the home page.

    Args:
        categories: DataFrame containing category data.
        categories_path: Path to the categories CSV file.
        project_id: ID of the project to filter categories for.
    """
    # Print information
    print("Categories:")
    print(
        csv_utils.get_row(categories, "project_id", project_id).to_string(index=False)
    )

    # Get action
    print(
        "\n\nWould you like to add a category(1), edit a category(2), or return to home page(3)"
    )
    action = int(input())

    match action:
        case 1:
            add_categories(categories, categories_path, project_id)
        case 2:
            edit_categories(categories, categories_path)
        case 3:
            print("Returning to home page")


def add_categories(
    categories: pd.DataFrame, categories_path: str | Path, project_id: int
) -> None:
    """Add a new category to a project.

    Prompts for a category name and appends a new row with the given
    project ID to the categories DataFrame.

    Args:
        categories: DataFrame containing category data.
        categories_path: Path to the categories CSV file.
        project_id: ID of the project to associate the category with.
    """
    # Get category information
    print("What is the name of the new category")
    category_name = input()

    # Update information
    categories = csv_utils.add_row(
        [len(categories), category_name, project_id, None, None], categories
    )
    csv_utils.write_data([categories_path], [categories])


def edit_categories(categories: pd.DataFrame, category_path: str | Path) -> None:
    """Edit a category's name, best version, or best revision.

    Prompts for a category ID, the field to edit, and the new value,
    then saves the change to the CSV file.

    Args:
        categories: DataFrame containing category data.
        category_path: Path to the categories CSV file.
    """
    # Get category to edit
    print("Enter ID of category to edit")
    category_id = int(input())

    # Get edit value
    print("Would you like to edit the name(1), best version(2), or best revision(3)")
    edit_type = int(input())
    print("Enter new value")
    new_value = input()

    match edit_type:
        case 1:
            column = "category_name"
        case 2:
            column = "best_version"
        case 3:
            column = "best_revision"

    # Save change
    categories = csv_utils.change_cell(
        categories, "category_id", category_id, column, new_value
    )
    csv_utils.write_data([category_path], [categories])
