# Goals: Starting off with a basic task manager project
# Add task
# Edit task
# Remove Task 
# Add/Remove task note
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
            print('TODO')
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
    print('Removing', tasks[int(task_num)])

    tasks.remove(tasks[int(task_num)-1])
    print('Removed \n')
    displayTasks(tasks)

    # bring back to menu
    menu(tasks)

# Main application 
menu(tasks)