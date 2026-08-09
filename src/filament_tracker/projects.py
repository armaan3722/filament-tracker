from filament_tracker import csv_utils


# PROJECTS
def read_projects(projects_path, categories_path):
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


def add_project(projects, projects_path):
    # Get information about new project
    print("What is the new project name")
    name = input()

    # Update information
    projects = csv_utils.add_row([len(projects), name], projects)
    csv_utils.write_data([projects_path], [projects])


def edit_project(projects, projects_path):
    # Get project to edit
    print(projects.to_string(index=False))
    print("Enter ID of project to edit")
    project_id = int(input())

    # Get new project name
    print("Enter new project name")
    name = input()

    # Save data
    projects = csv_utils.change_cell(
        projects, "project_id", project_id, "project_name", name
    )
    csv_utils.write_data([projects_path], [projects])


# CATEGORIES
def read_categories(categories, categories_path, project_id):
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


def add_categories(categories, categories_path, project_id):
    # Get category information
    print("What is the name of the new category")
    category_name = input()

    # Update information
    categories = csv_utils.add_row(
        [len(categories), category_name, project_id, None, None], categories
    )
    csv_utils.write_data([categories_path], [categories])


def edit_categories(categories, category_path):
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
