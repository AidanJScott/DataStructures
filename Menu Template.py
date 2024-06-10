# Creator: Aidan Scott
# Date: 6/9/24
# Description: This program serves as a basic menu template with
# validation loops to ensure proper user inputs

# global constants
WELCOME_MESSAGE = "WELCOME MESSAGE, \n\tPRESS ENTER TO CONTINUE"

# menu text
FIRST_MENU_OPTION = "FIRST MENU OPTION"
SECOND_MENU_OPTION = "SECOND MENU OPTION"
THIRD_MENU_OPTION = "THIRD MENU OPTION"
FOURTH_MENU_OPTION = "FOURTH MENU OPTION"
EXIT_MENU_OPTION = "EXIT MENU OPTION"

# menu values
VALUE_FIRST_MENU = "1"
VALUE_SECOND_MENU = "2"
VALUE_THIRD_MENU = "3"
VALUE_FOURTH_MENU = "4"

# choice values align with the min and max numbers displayed in the menu
LOW_CHOICE_VALUE = 1
HIGH_CHOICE_VALUE = 4

PROMPT_MENU_CHOICE = "Please enter an option (1, 2, etc.) or enter X to exit: "

ERROR_INVALID_CHOICE = "Error: Invalid menu choice"

def printMenu():
    """
    Prints the contents of the menu.
    Takes no parameters and returns no values
    """
    print("1. " + FIRST_MENU_OPTION)
    print("2. " + SECOND_MENU_OPTION)
    print("3. " + THIRD_MENU_OPTION)
    print("4. " + THIRD_MENU_OPTION)
    print("X. " + EXIT_MENU_OPTION)

    return

def main():
    """
    Displays an interactive basic menu. 
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
            printMenu()

            # collect user input
            menuChoice = input(PROMPT_MENU_CHOICE)

            # exit the menu
            if menuChoice.upper() == "X":
                exitMenu = True
                validChoice = True

            # check if the choice is within the bounds of the menu choice
            elif menuChoice.isnumeric():
                if LOW_CHOICE_VALUE <= int(menuChoice) <= HIGH_CHOICE_VALUE:
                    validChoice = True
                else:
                    print(ERROR_INVALID_CHOICE)
            else: 
                print(ERROR_INVALID_CHOICE)

        # execute the code for each menu option
        if menuChoice == VALUE_FIRST_MENU:
            print("\nExecuted first menu option\n")
        elif menuChoice == VALUE_SECOND_MENU:
            print("\nExecuted second menu option\n")
        elif menuChoice == VALUE_THIRD_MENU:
            print("\nExecuted third menu option\n")
        elif menuChoice == VALUE_FOURTH_MENU:
            print("\nExecuted fourth menu option\n")

if __name__ == "__main__":
    main()

