# Creator: Aidan Scott
# Date: 6/14/24
# Description: Generates the data that is used for the
# existing set of data in the main program.
# ONLY RUN ONE TIME TO GET THE DATA, IT WILL OVERRIDE THE EXISTING TEXT FILES

# global constants
ID_LOWER_BOUND = 10000000
ID_UPPER_BOUND = 99999999
FALSE_ID_LOWER_BOUND = 100000000
FALSE_ID_UPPER_BOUND = 999999999
SHORT_ID_COUNT = 1000
MEDIUM_ID_COUNT = 10000
LONG_ID_COUNT = 500000
LIST_SIZE_DIVISOR = 100

SHORT_LIST_FILENAME = "listOfIdsShort.txt"
SHORT_LOOKUP_FILENAME = "lookupListShort.txt"
MEDIUM_LIST_FILENAME = "listOfIdsMedium.txt"
MEDIUM_LOOKUP_FILENAME = "lookupListMedium.txt"
LONG_LIST_FILENAME = "listOfIdsLong.txt"
LONG_LOOKUP_FILENAME = "lookupListLong.txt"

import random

def generateIdList(idList, size):
    """
    Generate a list of unique ID's given a list size
    :param idList (list): list for the IDs to be added to
    :param size (int): the amount of IDs to be added to the list
    :return: None
    """
    for i in range(size):
        numberUsed = False
        while not numberUsed:
            randomId = random.randint(ID_LOWER_BOUND, ID_UPPER_BOUND)

            if randomId not in idList:
                idList.append(randomId)
                numberUsed = True

    return

def generateFalseIdList(someList, size):
    """
    Generates a list of false ID's one digit longer than real ID's
    given the size of the original list of ID's
    :param someList: The list for the false ID's to be added to the text file
    :param size: The size of the original list of ID's
    :return: None
    """
    # generate one false ID for every LIST_SIZE_DIVISOR real ID's
    for i in range(size // LIST_SIZE_DIVISOR):
        numberUsed = False
        while not numberUsed:

            randomId = random.randint(FALSE_ID_LOWER_BOUND, FALSE_ID_UPPER_BOUND)

            if randomId not in someList:
                someList.append(randomId)
                numberUsed = True

    return

def mergeLists(someList, otherList):
    """
    Merges two lists by placing the contents of
        the smaller list at somewhat regular intervals
        between the items in the larger list in a new list.
    :param someList: A nonempty list
    :param otherList: A nonempty list
    :return: Merged List
    """
    # swap lists to ensure someList is larger
    if len(someList) < len(otherList):
        temp = someList
        someList = otherList
        otherList = temp

    mergedList = []

    finalListLength = 0
    someListLength = 0
    otherListLength = 0

    interval = len(someList) // len(otherList)

    while finalListLength < len(someList) + len(otherList):

        insertIndex = random.randint(0, interval)

        # append values up to the insert index
        for i in range(0, insertIndex - 1):
            if someListLength < len(someList):
                mergedList.append(someList[someListLength])
                someListLength += 1
                finalListLength += 1

        # append the value from the smaller list
        if otherListLength < len(otherList):
            mergedList.append(otherList[otherListLength])
            otherListLength += 1
            finalListLength += 1

        # append the values up to the end of the interval
        for i in range(insertIndex, interval):
            if someListLength < len(someList):
                mergedList.append(someList[someListLength])
                someListLength += 1
                finalListLength += 1

    return mergedList

def writeListToFile(someList, file):
    """
    Writes the contents of a list to a file
        where each element is written on a new line
    :param someList (list):
    :param file: The file for the list to be written to
    :return: None
    """
    for element in someList:
        file.write(str(element) + "\n")

    return

def main():
    """
    Generate the text files for the existing set of ID's in the main program
    """

    shortFile = open(SHORT_LIST_FILENAME, "w")
    mediumFile = open(MEDIUM_LIST_FILENAME, "w")
    longFile = open(LONG_LIST_FILENAME, "w")

    shortList = []
    mediumList = []
    longList = []

    # generate lists of unique 8-digit ID's given the amount of ID's
    generateIdList(shortList, SHORT_ID_COUNT)
    generateIdList(mediumList, MEDIUM_ID_COUNT)
    generateIdList(longList, LONG_ID_COUNT)

    # write the contents of each list to all three respective files
    writeListToFile(shortList, shortFile)
    writeListToFile(mediumList, mediumFile)
    writeListToFile(longList, longFile)

    shortFile.close()
    mediumFile.close()
    longFile.close()

    shortFalseIdList = []
    mediumFalseIdList = []
    longFalseIdList = []

    # generate lists of 9-digit false ID's
    generateFalseIdList(shortFalseIdList, SHORT_ID_COUNT)
    generateFalseIdList(mediumFalseIdList, MEDIUM_ID_COUNT)
    generateFalseIdList(longFalseIdList, LONG_ID_COUNT)

    # merge the list of real and false ID's
    shortLookupList = mergeLists(shortList, shortFalseIdList)
    mediumLookupList = mergeLists(mediumList, mediumFalseIdList)
    longLookupList = mergeLists(longList, longFalseIdList)

    shortLookup = open(SHORT_LOOKUP_FILENAME, "w")
    mediumLookup = open(MEDIUM_LOOKUP_FILENAME, "w")
    longLookup = open(LONG_LOOKUP_FILENAME, "w")

    writeListToFile(shortLookupList, shortLookup)
    writeListToFile(mediumLookupList, mediumLookup)
    writeListToFile(longLookupList, longLookup)

    shortLookup.close()
    mediumLookup.close()
    longLookup.close()

    return

if __name__ == "__main__":
    main()