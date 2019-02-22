# -------------------------------------------------#
# Title: Working with Dictionaries, Todo.py
# Dev:   Tyler Ray
# Date:  2/21/21
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Tyler Ray, 02/21/2019, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#
# Declare variables
dicRow = {}
strChoice = None
lstTable = []
# Step a1 - Load data from a file
objFile = open("Todo.txt", 'r')
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
# Step 2 - Display a menu of choices to the user
# Option 5 to close the program is hidden in the menu options. Rather than
# having a block of code dedicated to closing the program, it's hardwired
while strChoice != '5':
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()
    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        # Use a for loop to run through dicRow and generically return keys and values [key]
        for key in dicRow:
            print(key + ', ' + dicRow[key])

        # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Prompt the user for a new task
        newTask = input("What task? ")
        # Check to see if the task is already in the dictionary
        if newTask not in dicRow:
            # Promot user for priority
            newPriority = input("What priority? ")
            # Combine new task and new priority into a dictionary item
            dicRow[newTask] = newPriority
            # Repeat what happened back to the user
            print(newTask, ':', newPriority, "has been added to the list.")
        # If th task was already in the dicitnary, it prints the following:
        else:
            print("That task is already on the list.")

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
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

    # Step 6 - Save tasks to the Todo.txt file
    elif (strChoice == '4'):
        print("Saving list to disk...")
        # Opening the file with 'w' so that I can write on it.
        objFile = open('Todo.txt', 'w')
        # I need to isolate keys and values from rowDic then save them in
        # the format I need so that my beginning code can pick up where
        # we leave off here
        for keys, values in dicRow.items():
            objFile.write(str(keys) + ',' + str(values) + '\n')
        objFile.close()
        print("Save complete!")
        quit()
# Program exits if '5' is input into menu
print("Goodbye")