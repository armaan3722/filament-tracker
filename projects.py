import csvUtils as csvUtils

# PROJECTS
def readProjects(projectsPath, categoriesPath):
    # Get dataframe
    projects, categories = csvUtils.readData([projectsPath, categoriesPath])

    # Print dataframe
    print('Projects:')
    print(projects.to_string(index=False))

    # Get action
    print('\n\nWould you like to add a project(1), edit a project(2), view categories for a project(3), or return to home page(4)')
    action = int(input())

    match action:
        case 1:
            addProject(projects, projectsPath)
        case 2:
            editProject(projects, projectsPath)
        case 3:
            print('Enter ID of project to view categories for')
            projectID = int(input())
            readCategories(categories, categoriesPath, projectID)
        case 4:
            print('Returning to home page')

def addProject(projects, projectsPath):
    # Get information about new project
    print('What is the new project name')
    name = input()

    # Update information
    projects = csvUtils.addRow([len(projects),name], projects)
    csvUtils.writeData([projectsPath], [projects])

def editProject(projects, projectsPath):
    # Get project to edit
    print(projects.to_string(index=False))
    print("Enter ID of project to edit")
    projectID = int(input())
    
    # Get new project name
    print('Enter new project name')
    name = input()

    # Save data
    projects = csvUtils.changeCell(projects, 'projectID', projectID, 'projectName', name)
    csvUtils.writeData([projectsPath], [projects])

# CATEGORIES
def readCategories(categories, categoriesPath, projectID):
    # Print information
    print('Categories:')
    print(csvUtils.getRow(categories, 'projectID', projectID).to_string(index=False))
    
    # Get action
    print('\n\nWould you like to add a category(1), edit a category(2), or return to home page(3)')
    action = int(input())

    match action:
        case 1:
            addCategories(categories, categoriesPath, projectID)
        case 2:
            editCategories(categories, categoriesPath)
        case 3:
            print('Returning to home page')
    
def addCategories(categories, categoriesPath, projectID):
    # Get category information
    print('What is the name of the new category')
    categoryName = input()

    # Update information
    categories = csvUtils.addRow([len(categories),categoryName,projectID,None,None], categories)
    csvUtils.writeData([categoriesPath], [categories])

def editCategories(categories, categoryPath):
    # Get category to edit
    print('Enter ID of category to edit')
    categoryID = int(input())

    # Get edit value
    print('Would you like to edit the name(1), best version(2), or best revision(3)')
    editType = int(input())
    print('Enter new value')
    newValue = input()

    match editType:
        case 1:
            column = 'categoryName'
        case 2:
            column = 'bestVersion'
        case 3:
            column = 'bestRevision'
    
    # Save change
    categories = csvUtils.changeCell(categories, 'categoryID', categoryID, column, newValue)
    csvUtils.writeData([categoryPath], [categories])