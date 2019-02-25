# -------------------------------------------------#
# Title: Working with Dictionaries, Todo.py
# Dev:   Tyler Ray
# Date:  2/21/21
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Tyler Ray, 02/21/2019, Added code to complete assignment 5
#   Tyler Ray, 2/24/2019, incorperated functions into the script
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

#----------------- Functions ---------------------#

#class menuClass has 5 function contained within
class menuClass():
    @staticmethod
# Function [1/5] of menuClass - The Menu
    def menuFunc(): # Holds the main menu for the program
        print(
            """
            Menu of Options
            1) Show current data
            2) Add a new item.
            3) Remove an existing item.
            4) Save Data to File
            5) Exit Program
            """)
        userChoice = str(input("Which option would you like to perform? [1 to 5] - "))
        return userChoice

    # Function [2/5] of menuClass - Show Tasks
    def showTasksFunc(): # Option 1, showing the tasks
        print('''
                        These are your tasks and their priority.
                        ''')
        for key in dicRow:
            print(key + ', ' + dicRow[key])

    # Function [3/5] of menuClass - Add Task
    def newTaskFunc(): # This function creats a new task,priority pair
        newTask = input("Task to add: ")
        if newTask not in dicRow:
            # Promot user for priority
            newPriority = input("Task priority: ")
            # Combine new task and new priority into a dictionary item
            dicRow[newTask] = newPriority
            # Repeat what happened back to the user
            print(newTask, ':', newPriority, "has been added to the list.")
        # If th task was already in the dicitnary, it prints the following:
        else:
            print("That task is already on the list.")

    # Function [4/5] of menuClass - Remove Task
    def removeTaskFunc(): # This function will delete a task and priority from the list
        # Prompt user to input a task to remove
        removeTask = input("What task do you want to delete? ")
        # Check to see if the task is already in the dictionary
        if removeTask in dicRow:
            # Deletes task from dictionary
            del dicRow[removeTask]
            # Repeats back to the user what happened
            print(removeTask, "deleted.")
        else:
            # if task isn't in dictionary, print this:
            print("That task isn't on the list.")

    # Function [5/5] of menuClass - Save File
    def saveTaskFunc(): # This function saves the list to the .txt file
        print("Saving list to disk...")
        textFileClass.objFileWriteFunc(fileName = "Todo.txt")
        # Opening the file with 'w' so that I can write on it.


# Class textFileClass has two function in it
class textFileClass():
    @staticmethod
    # Function [1/2] of textFileClass
    def objFileOpenFunc(fileName):
        objFile = open(fileName, 'r')
        # The starting data is already in comma separated and separate line table format
        # so I select for line in file
        for line in objFile.readlines():
            # split the line using the comma as a deliniator
            row = line.split(',')
            # take the 0th index, assign chore
            task = row[0]
            # take the 1st index, assign priority
            priority = row[1].strip("{}")
            # count the length of the variable priority, and subtract by 1 otherwise this will include \n
            noNewLine = len(priority) - 1
            # assign new value without \n back onto priority
            priority = priority[0:noNewLine]
            # add key and value pairs to dictionary
            dicRow[task] = priority

            # Once the data from the .txt file is loaded into memory in the format
            # I need, I close the file
        objFile.close()
    # Function [2/2] of textFileClass
    def objFileWriteFunc(fileName): # This function writes to fileName and is called in menuClass.saveTastFunc
        objFile = open(fileName,'w')
        # I need to isolate keys and values from rowDic then save them in
        # the format I need so that my beginning code can pick up where
        # we leave off here
        for keys, values in dicRow.items():
            objFile.write(str(keys) + ',' + str(values) + '\n')
        objFile.close()
        print("Save complete!")
        quit()

#----------------- Variables ---------------------#

dicRow = {} # Used to store data when txt file is opened and used to include new data in put
strChoice = None # The variable used for menu navigation
lstTable = [] #
objFile = textFileClass.objFileOpenFunc(fileName = "Todo.txt")

#----------------- Presention (I/O) ---------------------#

while strChoice != '5':
    strChoice = menuClass.menuFunc()

    if strChoice.strip() == '1':
        menuClass.showTasksFunc()
    elif (strChoice.strip() == '2'):
        menuClass.newTaskFunc()
    elif (strChoice == '3'):
        menuClass.removeTaskFunc()
    elif (strChoice == '4'):
        menuClass.saveTaskFunc()

print("Youre Data was not saved, goodbye.")