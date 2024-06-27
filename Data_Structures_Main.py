# Creator: Aidan Scott
# Date: 6/14/24
# Description: Main program shows the comparisons between
# different data structures in inserting and searching for items

# global constants
WELCOME_MESSAGE = "Data Structures Implementation, \nCreated by Aidan Scott\n\tPRESS ENTER TO CONTINUE"

# menu text
FIRST_MENU_OPTION = "Linked Lists"
SECOND_MENU_OPTION = "Trees"
THIRD_MENU_OPTION = "Hash Tables"
EXIT_MENU_OPTION = "Exit Program"
PROMPT_MAIN_MENU_CHOICE = "Please enter an option (1, 2, etc.) or enter X to exit: "
PROMPT_GENERAL_MENU_CHOICE = "Please enter an option (1, 2, etc.)"
ERROR_INVALID_CHOICE = "Error: Invalid menu choice"
PROMPT_FILE_CHOICE = "Choose a file size to process: "
SHORT_FILE_OPTION = "Short File: 1,000 Records"
MEDIUM_FILE_OPTION = "Medium File: 10,000 Records"
LONG_FILE_OPTION = "Long File: 500,000 Records"
LONG_FILE_WARNING = "WARNING: Long file should only be used for Hash Tables and AVL Trees"
BINARY_SEARCH_TREE_OPTION = "Binary Search Tree"
AVL_TREE_OPTION = "AVL Tree"
HASH_TABLE_CHAINING_OPTION = "Hash Table with Chaining"
HASH_TABLE_PROBING_OPTION = "Hash Table with Probing"

# menu values
VALUE_LINKED_LIST = "1"
VALUE_TREES = "2"
VALUE_HASH_TABLE = "3"
VALUE_BINARY_SEARCH_TREE = "1"
VALUE_AVL_TREE = "2"
VALUE_HASH_TABLE_CHAINING = "1"
VALUE_HASH_TABLE_PROBING = "2"
VALUE_SHORT_SIZE = "1"
VALUE_MEDIUM_SIZE = "2"
VALUE_LONG_SIZE = "3"


# choice values align with the min and max numbers displayed in the main menu
LOW_BOUND_MAIN_MENU = 1
HIGH_BOUND_MAIN_MENU = 3
LOW_BOUND_FILE_MENU = 1
HIGH_BOUND_FILE_MENU = 3
LOW_BOUND_STRUCTURE_TYPE_MENU = 1
HIGH_BOUND_STRUCTURE_TYPE_MENU = 2

# filenames
SHORT_LIST_FILENAME = "listOfIdsShort.txt"
SHORT_LOOKUP_FILENAME = "lookupListShort.txt"
MEDIUM_LIST_FILENAME = "listOfIdsMedium.txt"
MEDIUM_LOOKUP_FILENAME = "lookupListMedium.txt"
LONG_LIST_FILENAME = "listOfIdsLong.txt"
LONG_LOOKUP_FILENAME = "lookupListLong.txt"

from Linked_List import LinkedList
from Trees import BinaryTree, BinarySearchTree, AVLTree
from Hashing import HashTableProbing, HashTableChaining
import time

def printMainMenu():
    """
    Prints the contents of the main menu.
    Takes no parameters and returns no values
    """
    print("\n1. " + FIRST_MENU_OPTION)
    print("2. " + SECOND_MENU_OPTION)
    print("3. " + THIRD_MENU_OPTION)
    print("X. " + EXIT_MENU_OPTION)

    return

def printFileMenu():
    """
    Prints the contents of the file choice menu.
    Takes no parameters and returns no values
    """
    print("\n1. " + SHORT_FILE_OPTION)
    print("2. " + MEDIUM_FILE_OPTION)
    print("3. " + LONG_FILE_OPTION)
    print(LONG_FILE_WARNING)

    return

def printStructureTypeMenu(choices):
    """
    Prints the contents of the structure type choice menu.
    :param choices (tuple): a tuple containing strings of the menu options
    """
    print("\n1. " + choices[0])
    print("2. " + choices[1])

    return

def getFileSize():
    """
    Displays interactive menu where user chooses the file size
    :return (string): String associated with the file size
    """
    validChoice = False
    # user input validation loop
    while not validChoice:
        # print the main menu
        printFileMenu()

        # collect user input
        choice = input(PROMPT_FILE_CHOICE)

        # check if the choice is within the bounds of the menu choice
        if choice.isnumeric():
            if LOW_BOUND_FILE_MENU <= int(choice) <= HIGH_BOUND_FILE_MENU:
                validChoice = True
            else:
                print(ERROR_INVALID_CHOICE)
        else:
            print(ERROR_INVALID_CHOICE)

    return choice

def getFileNames(fileSize):
    """
    Gets the names of the files given a file size and returns names
        in the form of a tuple where the existing ID's are first
        and the lookup ID's are second
    :param fileSize: String indicating the size of the file
    :return (tuple): Tuple containing the existing and lookup file names
    """
    if fileSize == VALUE_SHORT_SIZE:
        fileNames = tuple([SHORT_LIST_FILENAME, SHORT_LOOKUP_FILENAME])

    elif fileSize == VALUE_MEDIUM_SIZE:
        fileNames = tuple([MEDIUM_LIST_FILENAME, MEDIUM_LOOKUP_FILENAME])

    elif fileSize == VALUE_LONG_SIZE:
        fileNames = tuple([LONG_LIST_FILENAME, LONG_LOOKUP_FILENAME])

    return fileNames

def getStructureType(category):
    """
    Displays interactive menu where user chooses a specific data structure
    given a category of data structure
    :param category (string): Value that represents a category of data structure
    :return (string): A value associated with the user's choice of data structure
    """
    if category == VALUE_TREES:
        choices = tuple([BINARY_SEARCH_TREE_OPTION, AVL_TREE_OPTION])
    elif category == VALUE_HASH_TABLE:
        choices = tuple([HASH_TABLE_CHAINING_OPTION, HASH_TABLE_PROBING_OPTION])

    validChoice = False
    # user input validation loop
    while not validChoice:
        # print the main menu
        printStructureTypeMenu(choices)

        # collect user input
        choice = input(PROMPT_GENERAL_MENU_CHOICE)

        # check if the choice is within the bounds of the menu choice
        if choice.isnumeric():
            if LOW_BOUND_STRUCTURE_TYPE_MENU <= int(choice) <= HIGH_BOUND_STRUCTURE_TYPE_MENU:
                validChoice = True
            else:
                print(ERROR_INVALID_CHOICE)
        else:
            print(ERROR_INVALID_CHOICE)

    return choice

def runDemo(structureChoice):
    """
    Runs the demonstration of inserting data into a given data structure
    and looking up records within the data structure
    :param structureChoice (string): A value representing a category of data structure
    :return:
    """
    fileSize = getFileSize()
    fileNameTuple = getFileNames(fileSize)

    existingIds = open(fileNameTuple[0], "r")
    lookupIds = open(fileNameTuple[1], "r")

    if structureChoice == VALUE_LINKED_LIST:
        dataStructure = LinkedList()

    elif structureChoice == VALUE_TREES:
        choice = getStructureType(structureChoice)

        if choice == VALUE_BINARY_SEARCH_TREE:
            dataStructure = BinarySearchTree()

        elif choice == VALUE_AVL_TREE:
            dataStructure = AVLTree()

    elif structureChoice == VALUE_HASH_TABLE:
        choice = getStructureType(structureChoice)

        if choice == VALUE_HASH_TABLE_CHAINING:
            dataStructure = BinarySearchTree()

        elif choice == VALUE_HASH_TABLE_PROBING:
            dataStructure = AVLTree()

    insertStartTime = time.time()

    existingIdCount = 0
    # insert existing ID's into data structure
    for line in existingIds:
        id = line.strip()
        if structureChoice == VALUE_LINKED_LIST:
            dataStructure.append(int(id))

        elif choice == VALUE_AVL_TREE:
            dataStructure = dataStructure.insert(int(id))

        else:
            dataStructure.insert(int(id))

        existingIdCount += 1

    insertEndTime = time.time()

    findStartTime = time.time()

    lookupIdCount = 0
    # search for lookup ID's
    for record in lookupIds:
        lookup = record.strip()

        result = dataStructure.find(int(lookup))

        if fileSize != VALUE_LONG_SIZE:
            if result is not None:
                print(f"{result} found in the data structure")

            else:
                print("Record not found")

        lookupIdCount += 1

    findEndTime = time.time()

    # print out time it takes to find records
    print(f"\nTime to insert {existingIdCount} records is: {insertEndTime - insertStartTime} seconds")
    print(f"Time to insert {lookupIdCount} records is: {findEndTime - findStartTime} seconds")


    return

def main():
    """
    Interactive menu that allows for user to see how different
    data structures store and find data with time comparisons
    """
    # print welcome message
    input(WELCOME_MESSAGE)

    exitMenu = False
    # menu exit loop
    while not exitMenu:

        validChoice = False
        # user input validation loop
        while not validChoice:
            # print the main menu
            printMainMenu()

            # collect user input
            menuChoice = input(PROMPT_MAIN_MENU_CHOICE)

            # exit the menu
            if menuChoice.upper() == "X":
                exitMenu = True
                validChoice = True

            # check if the choice is within the bounds of the menu choice
            elif menuChoice.isnumeric():
                if LOW_BOUND_MAIN_MENU <= int(menuChoice) <= HIGH_BOUND_MAIN_MENU:
                    validChoice = True
                else:
                    print(ERROR_INVALID_CHOICE)
            else:
                print(ERROR_INVALID_CHOICE)

        # execute the code for associated menu option
        if not exitMenu:
            runDemo(menuChoice)


if __name__ == "__main__":
    main()

