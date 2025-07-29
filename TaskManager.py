# Goals: Starting off with a basic task manager project
# Add task
# Edit task
# Remove Task 
# Add/Remove task note
tasks = []

# Auxillary functions
def displayTasks(tasks):
    print('----------------- Your tasks -----------------')
    for index, task in enumerate(tasks):
        print(index+1, '-', task )
    print('----------------------------------')

# Task menu bar for operations
def menu(tasks):
    # Prompt user input
    action = input('Please select a number: \n \n 1 - Add task \n 2- Edit task \n 3 - Delete Task \n \n')
    # Switch statement (using match)
    match action:
        case '1':
            addTask(tasks)
        case '2':
            print('TODO: Edit task')
        case '3':
            deleteTask(tasks)
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

# Main application 
menu(tasks)