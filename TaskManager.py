# Goals: Starting off with a basic task manager project, then add complexity
# to do: Connect to a database to locally store task inputs 
tasks = []

# Auxillary functions
def displayTasks(tasks):
    print('----------------- Your tasks -----------------')
    if len(tasks) == 0:
        print('\n No current tasks. \n')
    else:
        for index, task in enumerate(tasks):
            print(index+1, '-', task )
    print('----------------------------------')

# Task menu bar for operations
def menu(tasks):
    # Prompt user input
    user_input = input('Please select a number: \n \n A - Add task \n V - View task list \n D - Delete Task \n E - Edit task \n Q - Quit \n \n')
    # convert input to lowercase to simplify the match action 
    action = user_input.lower()
    # Switch statement (using match)
    match action:
        case 'a':
            addTask(tasks)
        case 'v':
            displayTasks(tasks)
            menu(tasks)
        case 'd':
            deleteTask(tasks)
        case 'e':
            editTask(tasks)
        case 'q':
            print('Exiting program...')
            return 0
        case _:
            print('Invalid input, try again')
            menu(tasks)

# ----------- FUNCTION ACTIONS ----------------------------------------------------- #

# --------------- ADD -------------------------------------------------------------- #
def addTask(tasks):
    # Prompt user input and append to tasks
    new_task = input('Please add a task: ')
    tasks.append(new_task)

    # call to function to display tasks
    displayTasks(tasks)

    # bring back to menu
    menu(tasks)

# --------------- DELETE  ---------------------------------------------------------- #
def deleteTask(tasks):
    # Delete 1 task
    input_num = input('Enter the number corresponding to the task you would like to delete: ')
    task_num = int(input_num)-1

    #validate that user input is within bounds 
    #print('length: ', len(tasks))
    if task_num <= len(tasks):
        print('Removing', tasks[int(task_num)])
        tasks.remove(tasks[int(task_num)-1])
        print('Removed \n')
        displayTasks(tasks)
    else:
        print('ERROR: Input not within bounds. Nothing deleted. \n ')
    # bring back to menu
    menu(tasks)

# --------------- EDIT  ------------------------------------------------------------- #
def editTask(tasks):
    input_num = input('Please select the number of the task you would like to edit: ')
    edit_num = int(input_num)-1

    #validate that user input is within bounds 
    if edit_num <= len(tasks):
        new_task = input('Edit task: ')
        tasks[int(edit_num)] = new_task
        print('Task edited \n')
        displayTasks(tasks)
    else:
        print('ERROR: Input not within bounds. Nothing edited. \n ')
        
    # bring back to menu
    menu(tasks)
# Main application 
menu(tasks)