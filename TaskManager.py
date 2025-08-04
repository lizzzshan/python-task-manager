# Goals: Starting off with a basic task manager project, then add complexity
# to do: Connect to a database to locally store task inputs 

# SQL connector for database
# import mysql.connector

tasks = []
completedTasks = []

# Auxillary functions
def displayTasks(tasks):
    print('----------------------------------')
    if len(tasks) == 0:
        print('\n No current tasks. \n')
    else:
        for index, task in enumerate(tasks):
            print(index+1, '-', task )
    print('----------------------------------')

# Task menu bar for operations
def menu(tasks):
    # Prompt user input
    user_input = input('Please select a number: \n \n A - Add task \n V - View current task list \n D - Delete Task \n E - Edit task \n C - Mark completed \n J - View completed task list \n Q - Quit \n \n')
    # convert input to lowercase to simplify the match action 
    action = user_input.lower()
    # Switch statement (using match)
    match action:
        case 'a':
            addTask(tasks)
        case 'v':
            print('Your current tasks: ')
            displayTasks(tasks)
            menu(tasks)
        case 'd':
            deleteTask(tasks)
        case 'e':
            editTask(tasks)
        case 'c':
            markCompleted(tasks)
        case 'j':
            print('Your completed tasks: ')
            displayTasks(completedTasks)
            menu(completedTasks)
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

def markCompleted(tasks):
    # while task list is not empty
    if(len(tasks) > 0):

        input_task = input('Select completed task number: ')
        input_num = int(input_task) - 1

        # Store into completed tasks
        completedTasks.append(tasks[input_num])
        print('Your completed tasks: ')
        displayTasks(completedTasks)

        # Remove from current task list 
        tasks.remove(tasks[input_num])

        # print(tasks, completedTasks) # Debugging, checking global arrays
    else:
        print('ERROR! Task list is empty. \n')
    # bring back to menu
    menu(tasks)
# Main application 
menu(tasks)