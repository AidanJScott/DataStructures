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
SETTINGS_MENU_OPTION = "Settings"
EXIT_MENU_OPTION = "Exit Program"
SETTINGS_HASH_SIZE_OPTION = "Resize Hash Table"
SETTINGS_PRINT_RECORDS_OPTION = "Toggle Printing Records"
SETTINGS_EXIT_OPTION = "Exit Settings Menu"
HASH_SIZE_WARNING = "Warning: Prime numbers greater than the amount of records\nare recommended for the hash table size"
SHORT_FILE_OPTION = "Short File: 1,000 Records"
MEDIUM_FILE_OPTION = "Medium File: 10,000 Records"
LONG_FILE_OPTION = "Long File: 500,000 Records"
LONG_FILE_WARNING = "WARNING: Long file should only be used for Hash Tables and AVL Trees"
BINARY_SEARCH_TREE_OPTION = "Binary Search Tree"
AVL_TREE_OPTION = "AVL Tree"
HASH_TABLE_CHAINING_OPTION = "Hash Table with Chaining"
HASH_TABLE_PROBING_OPTION = "Hash Table with Probing"

PROMPT_MAIN_MENU_CHOICE = "Please enter an option (1, 2, S, etc.) or enter X to exit: "
PROMPT_GENERAL_MENU_CHOICE = "Please enter an option (1, 2, etc.): "
PROMPT_PRINT_TOGGLE_CHOICE = "Please enter 'Y' or 'N' to turn on or off record printing: "
PROMPT_HASH_TABLE_SIZE = "Please enter a positive integer for the size of the hash table: "
PROMPT_FILE_CHOICE = "Choose a file size to process: "
ERROR_INVALID_CHOICE = "Error: Invalid menu choice"

# menu values
VALUE_LINKED_LIST = "1"
VALUE_TREES = "2"
VALUE_HASH_TABLE = "3"
VALUE_PRINT_TOGGLE = "1"
VALUE_HASH_TABLE_SIZE = "2"
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
LOW_BOUND_SETTINGS_MENU = 1
HIGH_BOUND_SETTINGS_MENU = 2
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

DEFAULT_PRINT_TOGGLE = True
DEFAULT_HASH_TABLE_SIZE = 1000003
INDEX_PRINT_TOGGLE = 0
INDEX_HASH_TABLE = 1

from Linked_List import LinkedList
from Trees import BinaryTree, BinarySearchTree, AVLTree
from Hashing import HashTableProbing, HashTableChaining
import time

def settingsMenu(settingsList):
    """
    Displays an interactive settings menu where settings
        for the program can be adjusted.
    :param (list): List of the settings in the order of the settings menu
    :return: None
    """
    exitMenu = False
    # menu exit loop
    while not exitMenu:

        validChoice = False
        # user input validation loop
        while not validChoice:
            # print the main menu
            printSettingsMenu()

            # collect user input
            menuChoice = input(PROMPT_GENERAL_MENU_CHOICE)

            # exit the menu
            if menuChoice.upper() == "X":
                exitMenu = True
                validChoice = True

            # check if the choice is within the bounds of the menu choice
            elif menuChoice.isnumeric():
                if LOW_BOUND_SETTINGS_MENU <= int(menuChoice) <= HIGH_BOUND_SETTINGS_MENU:
                    validChoice = True
                else:
                    print(ERROR_INVALID_CHOICE)
            else:
                print(ERROR_INVALID_CHOICE)

            if menuChoice == VALUE_PRINT_TOGGLE:
                printToggle = getPrintToggleChoice()
                settingsList[INDEX_PRINT_TOGGLE] = printToggle

            elif menuChoice == VALUE_HASH_TABLE_SIZE:
                hashTableSize = getHashTableSize()
                settingsList[INDEX_HASH_TABLE] = hashTableSize


    return

def printMainMenu():
    """
    Prints the contents of the main menu.
    Takes no parameters and returns no values
    """
    print("\n1. " + FIRST_MENU_OPTION)
    print("2. " + SECOND_MENU_OPTION)
    print("3. " + THIRD_MENU_OPTION)
    print("S. " + SETTINGS_MENU_OPTION)
    print("X. " + EXIT_MENU_OPTION)

    return

def printSettingsMenu():
    """
    Prints the contents of the settings menu.
    Takes no parameters and returns no values
    """
    print("\n1. " + SETTINGS_PRINT_RECORDS_OPTION)
    print("2. " + SETTINGS_HASH_SIZE_OPTION)
    print("X. " + SETTINGS_EXIT_OPTION)

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

def getPrintToggleChoice():
    """
    Displays interactive menu where user chooses to toggle print statements.
        Returns True if the user chooses to print records found, False otherwise
    :return (boolean): True if records are chosen to be printed, False otherwise
    """
    validChoice = False
    # user input validation loop
    while not validChoice:
        # collect user input
        choice = input("\n" + PROMPT_PRINT_TOGGLE_CHOICE)

        # check if the choice is within the bounds of the menu choice
        if choice.upper() == "Y":
            toggle = True
            validChoice = True

        elif choice.upper() == "N":
            toggle = False
            validChoice = True

        else:
            print(ERROR_INVALID_CHOICE)

    return toggle

def getHashTableSize():
    """
    Displays interactive menu where user chooses the hash table size
    :return (int): The size of the hash table
    """
    validChoice = False
    # user input validation loop
    while not validChoice:

        # collect user input
        print("\n" + HASH_SIZE_WARNING)
        size = input(PROMPT_HASH_TABLE_SIZE)

        # check if the choice is within the bounds of the menu choice
        if size.isnumeric():
            validChoice = True
            size = int(size)
        else:
            print(ERROR_INVALID_CHOICE)

    return size

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

def runDemo(structureChoice, settingsList):
    """
    Runs the demonstration of inserting data into a given data structure
    and looking up records within the data structure
    :param structureChoice (string): A value representing a category of data structure
    :return:
    """
    printToggle = settingsList[0]
    hashTableSize = settingsList[1]

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

        hashTableSize = settingsList[1]

        if choice == VALUE_HASH_TABLE_CHAINING:
            dataStructure = HashTableChaining(hashTableSize)

        elif choice == VALUE_HASH_TABLE_PROBING:
            dataStructure = HashTableProbing(hashTableSize)

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

    printToggle = settingsList[0]

    lookupIdCount = 0
    # search for lookup ID's
    for record in lookupIds:
        lookup = record.strip()

        result = dataStructure.find(int(lookup))

        if fileSize != VALUE_LONG_SIZE and printToggle:
            if result is not None:
                print(f"{result} found in the data structure")

            else:
                print("Record not found")

        lookupIdCount += 1

    findEndTime = time.time()

    # print out time it takes to insert and find records
    print(f"\nTime to insert {existingIdCount} records is: {insertEndTime - insertStartTime} seconds")
    print(f"Time to insert {lookupIdCount} records is: {findEndTime - findStartTime} seconds")


    return

def main():
    """
    Interactive menu that allows for user to see how different
    data structures store and find data with time comparisons
    """
    # set default settings values
    printToggle = DEFAULT_PRINT_TOGGLE
    hashTableSize = DEFAULT_HASH_TABLE_SIZE
    settingsList = [printToggle, hashTableSize]

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

            elif menuChoice.upper() == "S":
                settingsMenu(settingsList)
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
        if not exitMenu and menuChoice.upper() != "S":
            runDemo(menuChoice, settingsList)


if __name__ == "__main__":
    main()

